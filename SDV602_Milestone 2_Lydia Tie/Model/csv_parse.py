import csv
import pandas as pd

def Total_Case_Dict(country, year, csv_path):
    
    with open(csv_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        my_dict = {"Date": [], "Newcases": []}
        new_dict = {"Date": [], "Newcases": []}
        
        for line in csv_reader:
            if line['location'] == country and str(year) in line['date']:                
                my_dict["Date"].append(line['date'])
                my_dict["Newcases"].append(line['new_cases'])

        for x in range(1, 100):
            new_dict['Date'].insert(0, my_dict['Date'][-x])
            new_dict['Newcases'].insert(0, int(float(my_dict['Newcases'][-x])))
        return new_dict

def get_country_name(csv_path):
    with open(csv_path, "r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        continent_lists = ['World', 'Africa', 'Asia', 'Europe', 'European Union', 'International', 'North America', 'Oceania', 'South America']
        country_lists = []

        for line in csv_reader:
            if line['continent'] != '':
                country_lists.append(line['location'])
                
        unique_country = set(country_lists)
        sorted_country = sorted(unique_country)
        final_list = continent_lists + sorted_country
        return final_list

def get_latest_date(csv_path):
     with open(csv_path, "r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        date_lists = []
        for line in csv_reader:
            if line['location'] == 'World':
                date_lists.append(line['date'])
        return date_lists[-1]
                
def calculate_death_rate(cases, deaths):
    death_rate = round(deaths/cases * 100, 2)
    return death_rate

def death_rates(choice, csv_path):
    df = pd.read_csv(str(csv_path), usecols= [2, 3, 4, 7], header=0)
    date = get_latest_date(csv_path)
    filt = (df['date'] == date)
    df = df[filt]
    df['mortality_rate'] = calculate_death_rate(df['total_cases'] , df['total_deaths'])
    df = df[['location', 'mortality_rate']]

    if choice == 'Highest death':
        result =df.sort_values('mortality_rate', ascending=False).head(5)
    elif choice == 'Lowest death':
        result =df.sort_values('mortality_rate', ascending=True).head(5)

    return result

def fully_vaccinated_rate(choice, csv_path):

    df = pd.read_csv(str(csv_path), usecols= [2, 41], names=['country', 'fvr'], header=0)
    
    vaccinated = df.groupby('country').max()['fvr']


    if choice == 'Highest vaccinated':
        result = vaccinated.nlargest(10)
        df = result.to_frame().reset_index()

    elif choice == 'Lowest vaccinated':
        result = vaccinated.nsmallest(10)
        df = result.to_frame().reset_index()

    return df

def merge_csv(target, source, merge):

    df = pd.read_csv(str(target))
    df1 = pd.read_csv(str(source))

    date = pd.to_datetime(get_latest_date(target))
    date1 = pd.to_datetime(get_latest_date(source))

    filtered_df = df1.loc[df1['date'].between(str(date),str(date1))]

    df.to_csv(merge, index=False)
    
    filtered_df.to_csv(merge, mode="a", index=False, header=False)
    

    