import PySimpleGUI as sg
import View.merge as merge


def accept(event, values, window):
    keep_going = True
    if event == "Select Source CSV":
        file_name = sg.PopupGetFile('Please select source file to merge', file_types=(("Comma separated value", "*.csv"),))

        if file_name != None:
            window["-SOURCE-"].update(file_name)
            merge.source_file = file_name

    return keep_going
