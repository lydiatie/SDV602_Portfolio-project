import sys
sys.path.append(".")
import View.Des as Des
from Model.user_manager import UserManager

def accept( event, values, window):
    keep_going = True

    if event == '3. Vaccinated':
        a_user_manager = UserManager()
        UserManager.stop_thread = True
        result = a_user_manager.set_current_DES(3)
        window.close()
        Des.des(Des.columns("column3"), Des.title[2], Des.function[2], 3)
        keep_going = False
            
    return keep_going