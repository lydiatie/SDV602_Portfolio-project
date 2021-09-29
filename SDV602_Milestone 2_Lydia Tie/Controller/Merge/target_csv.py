import sys 
sys.path.append(".")
import PySimpleGUI as sg
import View.merge as merge

def accept( event, values, window):

    keep_going = True
    if event == "Select Target CSV":
        file_name = sg.PopupGetFile('Please select file to update (the target)', file_types=(("Comma separated value", "*.csv"),))

        if file_name != None:
            window["-TARGET-"].update(file_name)
            merge.target_file = file_name

    return keep_going
    