import sys
sys.path.append(".")
import View.Des as Des

def accept( event, values, window):
    keep_going = True

    if event == '1. Monthly new cases': #if user click on this button 
        window.close() #the menu window will close 
        Des.des(Des.columns("column1"), Des.title[0], Des.function[0]) #and open des 1 window
        keep_going = False

    return keep_going