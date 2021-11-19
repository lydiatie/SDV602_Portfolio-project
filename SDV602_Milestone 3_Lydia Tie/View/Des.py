import sys
sys.path.append(".")
import PySimpleGUI as sg
from threading import Thread
import Draw_plot as dp
import Controller.Des.win_closed as wc
import Controller.Des.send as send
import Controller.Des.back_button as back
import Controller.Des.submit as submit
import Controller.Des.merge as merge
import Controller.Des.plot as p 
from Model.user_manager import UserManager
from Model.csv_parse import get_country_name
import signal
import threading


a_user_manager = UserManager()

title = ['Daily new Covid cases', 'Death rates by country', 'Fully Vaccinated rates by country']

function = [dp.draw_des1_plot, dp.draw_des2_plot, dp.draw_des3_plot]

# exit_event = threading.Event()

# def signal_handler():
#     exit_event.set()

# signal.signal(signal.SIGINT, signal_handler)

def set_up_thread(window, desno):
    t = Thread(target=des_update, args=(window, desno,))
    t.setDaemon(True)
    UserManager.stop_thread = False
    t.start()

def des_update(window, desno):

    if not UserManager.stop_thread:
        update_user = a_user_manager.get_des_user(desno)
        window.write_event_value('-UPDATETHREAD-', update_user)

def columns(des_column):

    if des_column == "column1":
        csv = "test_data/owid-covid-data.csv"
        column = [[sg.Combo(values= get_country_name(csv), default_value= 'Select country', size=(12,1), pad=(0, 0), enable_events=True, key='-COMBO1-')],
                  [sg.Combo(values= get_country_name(csv),  default_value= 'Select country', size=(12,1), pad=((0,0),(10,0)), enable_events=True, key='-COMBO2-')],
                  [sg.Button('Plot', key='-UPDATE-', size=(10,1), pad=(0, 10))]]
        
    elif des_column == "column2":

        column = [[sg.Combo(('Highest death', 'Lowest death'), 'Highest death', size=(12,1), pad=((0,0),(0,20)), enable_events=True, key='-COMBO3-')],
                   [sg.Button('Plot', key='-UPDATE-', size=(10,1), pad=(0, 10))]]
 
    elif des_column == "column3":
        
        column = [[sg.Combo(('Highest vaccinated', 'Lowest vaccinated'), 'Highest vaccinated', size=(12,1), pad=((0,0),(0,20)), enable_events=True, key='-COMBO3-')],
                   [sg.Button('Plot', key='-UPDATE-', size=(10,1), pad=(0, 10))]]

    return column

def des(columns, win_title, func, desno):
    """
    This function creates DES window form.
    """
    des_user = a_user_manager.get_des_user(desno)
    chat_lists = a_user_manager.get_chat(desno)

    # create an output and multiline text in a column for text chat system
    chat_room = [[sg.Multiline(chat_lists, autoscroll=True, key='-CHATDISPLAY-',size=(65, 5))],
                 [sg.Input(tooltip='Type to chat', key='-MSG-',size=(55,1)), sg.Button('Send', key='-SEND-')]]

    users_online = [[sg.Text(f'Users in DES {desno}',  text_color='black', font='Helvetica 12')], 
                    [sg.Listbox((des_user), key= "-DES-", size=(15, 5))]]

    # define the window layout
    layout = [[sg.Button('Back', size=(12,1)), sg.Text(" ", size=(43,1)), sg.Button("Download and Merge latest data", key="-DOWNLOAD-")],
              [sg.Canvas(size=(400, 40), key='-CONTROLS-')],
              [sg.Canvas(size=(320 * 2, 350), key='-CANVAS-', background_color='#DAE0E6'), sg.Col(columns, element_justification='c')],
              [sg.Col(chat_room, pad=((0, 0),(10,0))), sg.Col(users_online, element_justification='c')]
             ]

    # create the DES window form and show it without the plot
    window = sg.Window(win_title, layout, size=(800, 600), font='Helvetica 12', finalize=True)
    set_up_thread(window, desno)

    keep_going = True
    figure_agg = None
    

    while keep_going == True:
        event, values = window.read()

        keep_going = send.accept(event, values, window)
        keep_going = back.accept(event, window, figure_agg)
        keep_going = submit.accept(event, values, window)
        keep_going = merge.accept(event)

        keep_going = wc.accept(event, values, window)
        if keep_going == False:
            break

        result = p.accept(event, values, window, func, figure_agg)
            
        keep_going = result[0]
        figure_agg = result[1]

        if event == '-UPDATETHREAD-' and not UserManager.stop_thread:
            UserManager.stop_thread = True
            new_chat_lists = a_user_manager.get_chat(desno)
            
            window.Element('-DES-').Update(values[event])
            window['-CHATDISPLAY-'].Update(new_chat_lists)

            if UserManager.stop_thread:
                UserManager.stop_thread = False
                set_up_thread(window, desno)


    window.close()


