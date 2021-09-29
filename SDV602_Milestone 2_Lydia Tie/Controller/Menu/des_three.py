import sys
sys.path.append(".")
import View.Des as Des

def accept( event, values, window):
    keep_going = True

    if event == '3. Vaccinated':
        window.close()
        Des.des(Des.columns("column3"), Des.title[2], Des.function[2])
        keep_going = False
            
    return keep_going