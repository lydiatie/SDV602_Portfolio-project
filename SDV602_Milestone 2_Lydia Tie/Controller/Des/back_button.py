import sys 
sys.path.append(".")
import View.Draw_plot as dp
import View.Menu as Menu



def accept( event, values, window):

    keep_going = True
    if event == 'Back':
        # if figure_agg:
        #     dp.delete_figure_agg(figure_agg)
        window.close()
        Menu.menu()
    return keep_going