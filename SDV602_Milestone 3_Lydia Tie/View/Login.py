import PySimpleGUI as sg
import sys
sys.path.append(".")
import Controller.Login.login_button as lb
import Controller.Login.register_page as rp
import Controller.Des.win_closed as wc

def login_view():

    layout = [[sg.Text("Please enter your username and password to login", pad = (0,20), justification="center", size = (25, 2), text_color='white', font='Helvetica 20')],
              [sg.Text("Username:", text_color='white', pad=((0, 250),(25, 0)))],
              [sg.Input(background_color="lightgray", key= "-USER-", size=(36, 1), pad=(0, 15))],
              [sg.Text("Password:", text_color='white', pad=((0,250),(0)))],
              [sg.Input(background_color="lightgray", key= "-PASSWORD-", password_char= "*",size=(36, 1), pad=(0, 15))],
              [sg.Button("Register", size=(10,2)), sg.Button("Login", button_color=('black', 'lightgray'), size=(15,2), pad=(10, 10))]]

    window = sg.Window("Login", layout, size=(500, 400), font='Helvetica 12', element_justification='c')

    controls = [lb.accept, rp.accept, wc.accept]
    keep_going = True
    while keep_going == True:

        event, value = window.read()

        for accept_controls in controls:
            keep_going = accept_controls(event, value, window)

            if keep_going == False: 
                break

    window.close()

if __name__ == '__main__':
    login_view()