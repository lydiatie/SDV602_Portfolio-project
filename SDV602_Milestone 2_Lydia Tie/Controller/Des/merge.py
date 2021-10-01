import sys
sys.path.append(".")
from View.merge import merge_window

def accept(event):
    keep_going = True
    if event == "Merge CSV files":
        merge_window()
    return keep_going