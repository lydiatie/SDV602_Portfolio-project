import sys
sys.path.append(".")
import View.Des as Des
from Model.user_manager import UserManager

def accept( event, values, window):
    keep_going = True

    if event == '1. Monthly new cases': #if user click on this button 
        a_user_manager = UserManager()
        UserManager.stop_thread = True
        result = a_user_manager.set_current_DES(1)
        window.close() #the menu window will close 
        Des.des(Des.columns("column1"), Des.title[0], Des.function[0], 1) #and open des 1 window
        keep_going = False

    return keep_going