import sys
sys.path.append(".")
import View.Des as Des
from Model.user_manager import UserManager

def accept( event, values, window):
    keep_going = True

    if event == '2. Death rates': 
        a_user_manager = UserManager()
        UserManager.stop_thread = True
        result = a_user_manager.set_current_DES(2)
        window.close()
        Des.des(Des.columns("column2"), Des.title[1], Des.function[1], 2)
        keep_going = False
            
    return keep_going