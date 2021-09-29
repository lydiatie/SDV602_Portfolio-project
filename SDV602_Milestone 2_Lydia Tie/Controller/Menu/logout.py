import PySimpleGUI as sg

def accept(event, value, window):
    keep_going = True
    
    if event in (sg.WIN_CLOSED, 'Logout'): 
        keep_going = False
    else:
        keep_going = True

    return keep_going