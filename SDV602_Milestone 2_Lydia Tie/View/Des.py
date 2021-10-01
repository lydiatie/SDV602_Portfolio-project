import sys
sys.path.append(".")
import PySimpleGUI as sg
import Draw_plot as dp
import Menu
from Model.csv_parse import get_country_name
from merge import merge_window
import Controller.Des.win_closed as wc
import Controller.Des.send as send
import Controller.Des.back_button as back
import Controller.Des.submit as submit
import Controller.Des.merge as merge
import Controller.Des.plot as p 


title = ['Daily new Covid cases', 'Death rates by country', 'Fully Vaccinated rates by country']

function = [dp.draw_des1_plot, dp.draw_des2_plot, dp.draw_des3_plot]

def columns(des_column):
    if des_column == "column1":
        column = [[sg.Combo(values=['Select country',], default_value= 'Select country', size=(12,1), pad=(0, 0), enable_events=True, key='-COMBO1-')],
                  [sg.Combo(values=['Select country',],  default_value= 'Select country', size=(12,1), pad=((0,0),(10,0)), enable_events=True, key='-COMBO2-')],
                  [sg.Button('Plot', key='-UPDATE-', size=(10,1), pad=(0, 10))]]
        
    elif des_column == "column2":

        column = [[sg.Combo(('Highest death', 'Lowest death'), 'Highest death', size=(12,1), pad=((0,0),(0,20)), enable_events=True, key='-COMBO3-')],
                   [sg.Button('Plot', key='-UPDATE-', size=(10,1), pad=(0, 10))]]
 
    elif des_column == "column3":
        
        column = [[sg.Combo(('Highest vaccinated', 'Lowest vaccinated'), 'Highest vaccinated', size=(12,1), pad=((0,0),(0,20)), enable_events=True, key='-COMBO3-')],
                   [sg.Button('Plot', key='-UPDATE-', size=(10,1), pad=(0, 10))]]

    return column


def des(columns, win_title, func):
    """
    This function creates DES window form.
    """
    
    # create an output and multiline text in a column for text chat system
    chat_room = [[sg.Output( background_color='white', size=(65, 4), text_color='black')],
                [sg.Multiline(size=(55,1), tooltip='Type to chat', focus = True, key='-MSG-', do_not_clear = False), sg.Button('Send')]]

    users_online = [[sg.Text('Users in DES 1',  text_color='black', font='Helvetica 12')], 
                    [sg.Listbox(['User C'], size=(15, 5))]]

    # define the window layout
    layout = [[sg.Button('Back', size=(12,1)), sg.Text("Choose a file: "), sg.Input(size=(27, 1)), sg.FileBrowse(key="-IN-", file_types=(("CSV Files", "*.csv"),)), sg.Button("Submit"), sg.Button("Merge CSV files")],
              [sg.Canvas(size=(400, 40), key='-CONTROLS-')],
              [sg.Canvas(size=(320 * 2, 350), key='-CANVAS-', background_color='#DAE0E6'), sg.Col(columns, element_justification='c')],
              [sg.Col(chat_room, pad=((0, 0),(10,0))), sg.Col(users_online, element_justification='c')]
             ]

    # create the DES window form and show it without the plot
    window = sg.Window(win_title, layout, size=(800, 600), font='Helvetica 12', finalize=True)
    keep_going = True
    figure_agg = None
    

    while keep_going == True:
        event, values = window.read()

        keep_going = wc.accept(event)
        if keep_going == False:
            break
        keep_going = send.accept(event, values)
        keep_going = back.accept(event, window, figure_agg)
        keep_going = submit.accept(event, values, window)
        keep_going = merge.accept(event)
 
        if figure_agg:
                # ** IMPORTANT ** Clean up previous drawing before drawing again
            dp.delete_figure_agg(figure_agg)

        result = p.accept(event, values, window, func)
            
        keep_going = result[0]
        figure_agg = result[1]
    
    window.close()


