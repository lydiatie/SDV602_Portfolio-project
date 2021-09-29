import sys
sys.path.append(".")
import View.Des as Des

def accept( event, values, window):
    keep_going = True

    if event == '2. Death rates': 
        window.close()
        Des.des(Des.columns("column2"), Des.title[1], Des.function[1])
        keep_going = False
            
    return keep_going