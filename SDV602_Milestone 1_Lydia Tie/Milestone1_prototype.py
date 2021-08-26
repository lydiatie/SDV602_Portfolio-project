import PySimpleGUI as sg
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
matplotlib.use('TkAgg')
import datetime
import pandas as pd

def draw_figure(canvas, figure):
    """
    This is Matplotlib helper code to draw a canvas in Pysimplegui window.
    """
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg

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

    while True:  # Event Loop
        event, values = window.read()
        print(event, values)
        if event in (sg.WIN_CLOSED, 'Logout'): 
            break
        elif event == '1. Monthly new cases': #if user click on this button 
            window.close() #the menu window will close 
            des_one() #and open des 1 window
        elif event == '2. Death rates': 
            window.close()
            des_two()
        elif event == '3. Vaccinated':
            window.close()
            des_three()

    window.close()

def draw_des1_plot(date, plot_A, plot_B):
    """
    This function is to draw the plot of DES 1.
    """ 
    #make up some data for the plot
    df = pd.DataFrame({'date': np.array([datetime.datetime(2020, 1, i+1)
                                     for i in range(12)]),
                   'Worldwide': [3, 4, 4, 7, 8, 9, 14, 17, 12, 8, 8, 13],
                   'Malaysia': [1, 1, 2, 3, 3, 3, 4, 3, 2, 3, 4, 7]})

    plt.xkcd() # comic style function 
 
    fig = plt.figure(figsize=(9, 6), dpi=35) # define the size of the figure
    fig.suptitle('Monthly new cases') # title of the chart

    ax = fig.add_subplot(111)
    # plot function to create 2 time series plots in a chart
    ax.plot(df[date], df[plot_A], label=plot_A, linewidth=3) 
    ax.plot(df[date], df[plot_B], color='red', label=plot_B, linewidth=3)
    # legend for 2 times series plots
    ax.legend() 
    ax.set_xlabel('Date') # define x axis label
    ax.set_ylabel('Cases per million people') # define y axis label
    return fig

def draw_des2_plot():
    """
    This function is to draw the plot of DES 2.
    """ 
    labels = ['USA', 'Brazil', 'India', 'Mexico', 'Peru']
    sizes = [31, 27, 21, 12, 9]
    plt.xkcd()

    fig = plt.figure(figsize=(9, 6), dpi=35)
    fig.suptitle('Highest death rates by country')

    ax = fig.add_subplot(111)
    ax.pie(sizes, labels=labels, autopct='%1.1f%%')
    ax.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.
    return fig

def draw_des3_plot():
    """
    This function is to draw the plot of DES 3.
    """ 
    objects = ('Singapore', 'Uruguay', 'Chile', 'Belgium', 'Denmark', 'Qatar', 'Portugal', 'Canada', 'Spain', 'Ireland')
    y_pos = np.arange(len(objects))
    performance = [71, 69, 68, 66, 65, 65, 64, 63, 63, 62]

    plt.xkcd()

    fig = plt.figure(figsize=(9, 6), dpi=35)
    fig.suptitle('Number of people fully vaccinated by country')
    ax = fig.add_subplot(111)
    ax.barh(y_pos, performance, align='center', alpha=0.5)
    plt.yticks(y_pos, objects)
    ax.set_xlabel('Share of people fully vaccinated')
    return fig

def des_one():
    """
    This function creates DES 1 window form.
    """
    # create two dropdown menus and two buttons in a column then use it in the layout using sg.Col(col1)
    col1 = [[sg.Combo(('Worldwide', 'Malaysia'), 'Select Country', size=(12,1), pad=(0, 0), enable_events=True, key='-COMBO1-')],
            [sg.Combo(('Worldwide', 'Malaysia'), 'Select Country', size=(12,1), pad=((0,0),(10,0)), enable_events=True, key='-COMBO2-')],
            [sg.Button('Zoom +/-', size=(10,1), pad=(0, 10))],
            [sg.Button('Pan', size=(10,1))]]
    # create an output and multiline text in a column for text chat system
    chat_room = [[sg.Output( background_color='white', size=(33, 4), text_color='black')],
                [sg.Multiline(size=(26,1), tooltip='Type to chat', focus = True, key='-MSG-', do_not_clear = False), sg.Button('Send')]]

    users_online = [[sg.Text('Users in DES 1',  text_color='black', font='Helvetica 12')], 
                    [sg.Listbox(['User C'], size=(15, 5))]]

    # define the window layout
    layout = [[sg.Button('Back', size=(12,1)), sg.Text(' ', size=(25, 1)), sg.Button('Upload data', size=(14,1))],
              [sg.Canvas(key='-CANVAS-', pad=(15,10)), sg.Col(col1, element_justification='c')],
              [sg.Col(chat_room, pad=((10, 0),(0,0))), sg.Col(users_online, element_justification='c')]
             ]

    # create the DES window form and show it without the plot
    window = sg.Window('Monthly new Covid cases', layout, size=(500, 400), font='Helvetica 12', finalize=True)

    # add the plot to the window
    draw_figure(window['-CANVAS-'].TKCanvas, draw_des1_plot('date', 'Malaysia', 'Worldwide'))

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        # if user click send button the input will display on the output screen
        elif event == 'Send':
            msg = values['-MSG-'].rstrip()
            print(f'{msg}')
        elif event == 'Back':
            window.close()
            menu()

    window.close()

def des_two():
    """
    This function creates DES 2 window form.
    """
    col1 = [[sg.Combo(('Highest death', 'Lowest death'), 'Highest death', size=(12,1), pad=((0,0),(0,20)))],
            [sg.Button('Zoom +/-', size=(10,1), pad=(0, 10))],
            [sg.Button('Pan', size=(10,1))]]

    chat_room = [[sg.Output( background_color='white', size=(33, 4), text_color='black')],
                [sg.Multiline(size=(26,1), tooltip='Type to chat', focus = True, key='-MSG-', do_not_clear = False), sg.Button('Send')]]

    users_online = [[sg.Text('Users in DES 2',  text_color='black', font='Helvetica 12')], 
                    [sg.Listbox(['User F'], size=(15, 5))]]

    layout = [[sg.Button('Back', size=(12,1)), sg.Text(' ', size=(25, 1)), sg.Button('Upload data', size=(14,1))],
            [sg.Canvas(key='-CANVAS-', pad=(15,10)), sg.Col(col1, element_justification='c')],
            [sg.Col(chat_room, pad=((10, 0),(0,0))), sg.Col(users_online, element_justification='c')]
            ]

    window = sg.Window('Death rates by country', layout, size=(500, 400), font='Helvetica 12', finalize=True)

    draw_figure(window['-CANVAS-'].TKCanvas, draw_des2_plot())

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'Send':
            msg = values['-MSG-'].rstrip()
            print(f'{msg}')
        elif event == 'Back':
            window.close()
            menu()

    window.close()

def des_three():
    """
    This function creates DES 3 window form.
    """
    col1 = [[sg.Combo(('Highest vaccinated', 'Lowest vaccinated'), 'Highest vaccinated', size=(12,1), pad=((0,0),(0,20)))],
            [sg.Button('Zoom +/-', size=(10,1), pad=(0, 10))],
            [sg.Button('Pan', size=(10,1))]]

    chat_room = [[sg.Output( background_color='white', size=(33, 4), text_color='black')],
                [sg.Multiline(size=(26,1), tooltip='Type to chat', focus = True, key='-MSG-', do_not_clear = False), sg.Button('Send')]]

    users_online = [[sg.Text('Users in DES 3',  text_color='black', font='Helvetica 12')], 
                    [sg.Listbox(['User H', 'User A'], size=(15, 5))]]

    layout = [[sg.Button('Back', size=(12,1)), sg.Text(' ', size=(25, 1)), sg.Button('Upload data', size=(14,1))],
            [sg.Canvas(key='-CANVAS-', pad=(15,10)), sg.Col(col1, element_justification='c')],
            [sg.Col(chat_room, pad=((10, 0),(0,0))), sg.Col(users_online, element_justification='c')]
            ]

    window = sg.Window('Vaccinated', layout, size=(500, 400), font='Helvetica 12', finalize=True)

    draw_figure(window['-CANVAS-'].TKCanvas, draw_des3_plot())

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'Send':
            msg = values['-MSG-'].rstrip()
            print(f'{msg}')
        elif event == 'Back':
            window.close()
            menu()

    window.close()    

if __name__ == '__main__':
    menu()