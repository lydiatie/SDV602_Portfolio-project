import sys
sys.path.append(".")
from Model.csv_parse import merge_csv

def accept(event):
    keep_going = True
    if event == "-DOWNLOAD-":
        merge_csv()
    return keep_going