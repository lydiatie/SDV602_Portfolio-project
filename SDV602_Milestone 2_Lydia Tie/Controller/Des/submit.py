import sys 
sys.path.append(".")
import PySimpleGUI as sg
from Model.csv_parse import get_country_name


def accept( event, values, window):
    keep_going = True
    if event == "Submit":
        csv_files = values["-IN-"]
    
        if window.Title == "Daily new Covid cases":
            try:
                window.find_element("-COMBO1-").update(value="Select country", values= get_country_name(csv_files))
                window.find_element("-COMBO2-").update(value="Select country", values= get_country_name(csv_files))

            except Exception as e:
                sg.Popup(e)
    return keep_going

