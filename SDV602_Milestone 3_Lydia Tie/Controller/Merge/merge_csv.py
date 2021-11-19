import sys 
sys.path.append(".")

import PySimpleGUI as sg
import os
import View.merge as merge
import Model.csv_parse as cp

def accept( event, values, window):

    keep_going = True
    if event == "Merge CSV":

        base_source_file = os.path.basename(merge.source_file)
        base_target_file = os.path.basename(merge.target_file)
        head_tail = os.path.split(merge.target_file)
        merge_directory = head_tail[0] + "/merged.csv"


        response = sg.PopupOKCancel(f'Merge {base_source_file} into {base_target_file}?') 
        if response == "OK":
            try:
                cp.merge_csv(merge.target_file, merge.source_file, merge_directory)
                sg.Popup("CSV files merged successfully. Save merged file as \'merged.csv\'")
            except Exception as e:
                sg.Popup(e)
    return keep_going
    