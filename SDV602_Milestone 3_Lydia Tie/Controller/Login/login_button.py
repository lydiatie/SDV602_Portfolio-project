import PySimpleGUI as sg
import sys
sys.path.append(".")
from Model.user_manager import UserManager


def accept(event, value, window):
    keep_going = True
    if event == 'Login':
        
        from View.Menu import menu
        a_user_manager = UserManager()

        user_name = value['-USER-']
        password = value['-PASSWORD-']      

        login_result = a_user_manager.login(user_name,password)

        if login_result == 'Login Success':
            sg.Popup(login_result)
            window.close()
            menu()
            keep_going = False
        else: 
            sg.Popup(login_result)
            keep_going = True

    return keep_going

