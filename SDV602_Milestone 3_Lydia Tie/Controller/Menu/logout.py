import PySimpleGUI as sg
from View.Login import login_view
from Model.user_manager import UserManager


def accept(event, value, window):
    keep_going = True
    
    if event in (sg.WIN_CLOSED, 'Logout'): 

        a_user_manager = UserManager()
        UserManager.stop_thread = True
        logout_result = a_user_manager.logout()

        sg.Popup(logout_result)
        
        window.close()
        login_view()
        keep_going = False
    else:
        keep_going = True

    return keep_going