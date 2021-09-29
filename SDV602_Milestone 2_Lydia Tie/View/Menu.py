import sys
sys.path.append(".")
import PySimpleGUI as sg
import Controller.Menu.logout as logout
import Controller.Menu.des_one as d1
import Controller.Menu.des_two as d2
import Controller.Menu.des_three as d3


def menu():
    """
    This function creates a menu window.
    """
    # create three buttons in a column then use it in the layout using sg.Col(col1)
    col1 = [ 
            [sg.Button('1. Monthly new cases', size=(18,2))], 
            [sg.Button('2. Death rates', size=(18,2))], 
            [sg.Button('3. Vaccinated', size=(18,2))]]

    # define the window layout
    layout = [[sg.Text('Welcome, User A', size=(20,1), text_color='black', font='Helvetica 18'), sg.Text(' ', size=(5,2)), sg.Button('Logout', size=(20, 1))],
              [sg.Text(' ')],
              [sg.Text('DES Menu', text_color='black', font='Helvetica 18', pad=(80,0)), sg.Text('Online User', text_color='black', font='Helvetica 18')],
              [sg.Col(col1, pad=(50,0)), sg.Listbox(('User A - DES 3', 'User C - DES 1', 'User F - DES 2', 'User H - DES 3'), size=(15, 10))]]

    #create the menu window form
    window = sg.Window('Menu', layout, size=(500, 400), font='Helvetica 12')
    
    controls = [logout.accept, d1.accept, d2.accept, d3.accept]
    keep_going = True

    while keep_going == True:  # Event Loop
        
        event, values = window.read()

        for accept_controls in controls:
            keep_going = accept_controls(event, values, window)

            if keep_going == False: 
                break

    window.close()

if __name__ == '__main__':

    menu()