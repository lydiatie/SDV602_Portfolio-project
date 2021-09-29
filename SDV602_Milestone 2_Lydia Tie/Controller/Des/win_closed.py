import PySimpleGUI as sg

def accept( event, values, window):
    keep_going = True
    if event == sg.WIN_CLOSED:
        keep_going = False
    else:
        keep_going = True
    return keep_going