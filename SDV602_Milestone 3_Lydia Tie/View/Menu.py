import sys
sys.path.append(".")
import PySimpleGUI as sg
from time import sleep
from threading import Thread
import Controller.Menu.logout as logout
import Controller.Menu.des_one as d1
import Controller.Menu.des_two as d2
import Controller.Menu.des_three as d3
from Model.user_manager import UserManager

a_user_manager = UserManager()

def set_up_thread(window):
    t = Thread(target=online_user_update, args=(window,))
    t.setDaemon(True)
    UserManager.stop_thread = False
    t.start()

def online_user_update(window):
    sleep(3)
    if not UserManager.stop_thread:
        update_user = a_user_manager.get_online_user()
        window.write_event_value('-UPDATETHREAD-', update_user)

def menu():
    """
    This function creates a menu window.
    """
    online_user = a_user_manager.get_online_user()
    current_user = a_user_manager.current_user

    # create three buttons in a column then use it in the layout using sg.Col(col1)
    col1 = [ 
            [sg.Button('1. Monthly new cases', size=(18,2))], 
            [sg.Button('2. Death rates', size=(18,2))], 
            [sg.Button('3. Vaccinated', size=(18,2))]]

    # define the window layout
    layout = [[sg.Text(f'Welcome, {current_user}', size=(20,1), text_color='black', font='Helvetica 18'), sg.Text(' ', size=(5,2)), sg.Button('Logout', size=(20, 1))],
              [sg.Text(' ')],
              [sg.Text('DES Menu', text_color='black', font='Helvetica 18', pad=(80,0)), sg.Text('Online User', text_color='black', font='Helvetica 18')],
              [sg.Col(col1, pad=(50,0)), sg.Listbox((online_user), key= "-ONLINE-", size=(15, 10))]]

    #create the menu window form
    window = sg.Window('Menu', layout, size=(500, 400), font='Helvetica 12')
    set_up_thread(window)
    
    controls = [logout.accept, d1.accept, d2.accept, d3.accept]
    keep_going = True

    while keep_going == True:  # Event Loop
        
        event, values = window.read()

        if event == '-UPDATETHREAD-' and not UserManager.stop_thread:
            UserManager.stop_thread = True
            
            window.Element('-ONLINE-').Update(values[event])

            if UserManager.stop_thread:
                UserManager.stop_thread = False
                set_up_thread(window)

        for accept_controls in controls:
            keep_going = accept_controls(event, values, window)

            if keep_going == False: 
                break

    window.close()
