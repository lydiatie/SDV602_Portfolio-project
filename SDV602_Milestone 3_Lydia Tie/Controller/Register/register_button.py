import PySimpleGUI as sg
import sys
sys.path.append(".")
from Model.user_manager import UserManager

def accept(event, value, window):
    keep_going = True
    if event == 'Register':
        a_user_manager = UserManager()

        user_name = value['-USER-']
        password = value['-PASSWORD-']

        register_result = a_user_manager.register(user_name, password)
        sg.Popup(f"{register_result}. Please go to login page to login")
    return keep_going