import PySimpleGUI as sg
import sys
sys.path.append(".")
from Model.user_manager import UserManager
import Controller.Register.register_button as rb
import Controller.Register.login_page as lp
import Controller.Des.win_closed as wc

def register_view():

    layout = [[sg.Text("Please enter your new username and password", pad = (0,20), justification="center", size = (20, 2), text_color='white', font='Helvetica 20')],
              [sg.Text("Username:", text_color='white', pad=((0, 250),(25, 0)))],
              [sg.Input(background_color="lightgray", key= "-USER-", size=(36, 1), pad=(0, 15))],
              [sg.Text("Password:", text_color='white', pad=((0,250),(0)))],
              [sg.Input(background_color="lightgray", key= "-PASSWORD-", password_char='*', size=(36, 1), pad=(0, 15))],
              [sg.Button("Login Page", key= "-LOGIN-", size=(10,2)), sg.Button("Register", button_color=('black', 'lightgray'), size=(15,2), pad=(10, 10))]]

    window = sg.Window("Register", layout, size=(500, 400), font='Helvetica 12', element_justification='c')

    controls = [rb.accept, lp.accept, wc.accept]
    keep_going = True

    while keep_going == True:

        event, value = window.read()

        for control in controls:
            keep_going = control(event, value, window)

            if keep_going == False: 
                break

    window.close()
