import sys 
sys.path.append(".")
import View.Draw_plot as dp
import View.Menu as Menu
from Model.user_manager import UserManager

def accept( event, window, figure_agg):

    keep_going = True
    if event == 'Back':
        a_user_manager = UserManager()
        UserManager.stop_thread = True
        result = a_user_manager.set_current_DES(0)
        if figure_agg:
            dp.delete_figure_agg(figure_agg)
        
        window.close()
        Menu.menu()

    return keep_going