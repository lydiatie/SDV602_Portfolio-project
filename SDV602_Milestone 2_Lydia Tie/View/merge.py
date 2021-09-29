import sys
sys.path.append(".")
import PySimpleGUI as sg
import Controller.Merge.exit as exit
import Controller.Merge.target_csv as target
import Controller.Merge.source_csv as source
import Controller.Merge.merge_csv as mc

target_file = ""
source_file = ""

def merge_window():

    layout = [[sg.Text('Upload data', font=('current 18'))],
            [sg.Text('Target File is:'), sg.Text('No data', key= "-TARGET-", size=(30,1))],
            [sg.Text('Source File is:'), sg.Text('No data', key= "-SOURCE-", size=(30,1))],
            [sg.Button("Select Target CSV", size=(10,2)), sg.Button("Select Source CSV", size=(10,2)), sg.Button("Merge CSV", size=(10,2)), sg.Exit(size=(5,2))]]

    ###Building Window
    window = sg.Window('My File Browser', layout)

    controls = [exit.accept, target.accept, source.accept, mc.accept]
    keep_going = True

    while keep_going == True:
        event, values = window.read()

        for accept_controls in controls:

            keep_going = accept_controls(event, values, window)

            if keep_going == False:
                break

        
    window.close()
