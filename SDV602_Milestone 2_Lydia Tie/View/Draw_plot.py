import sys
sys.path.append(".")
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
matplotlib.use('TkAgg')
import pandas as pd
import Model.csv_parse as cp

def draw_figure(canvas, figure, canvas_toolbar):
    """
    This is Matplotlib helper code to draw a canvas in Pysimplegui window.
    """
    if canvas.children:
        for child in canvas.winfo_children():
            child.destroy()
    if canvas_toolbar.children:
        for child in canvas_toolbar.winfo_children():
            child.destroy()
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    toolbar = Toolbar(figure_canvas_agg, canvas_toolbar)
    toolbar.update()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg

class Toolbar(NavigationToolbar2Tk):
    def __init__(self, *args, **kwargs):
        super(Toolbar, self).__init__(*args, **kwargs)

def delete_figure_agg(figure_agg):
    figure_agg.get_tk_widget().forget()
    plt.close('all')

def draw_des1_plot(plot_A, plot_B, csv):
    """
    This function is to draw the plot of DES 1.
    """ 
    #make up some data for the plot

    dictionary = pd.DataFrame(cp.Total_Case_Dict(plot_A, 2021, csv))
    dictionary1 = pd.DataFrame(cp.Total_Case_Dict(plot_B, 2021, csv))

    plt.xkcd() # comic style function 
 
    plt.figure(1)
    fig = plt.gcf()
    DPI = fig.get_dpi()
    fig.set_size_inches(320 * 2 / float(DPI), 350 / float(DPI))
    fig.suptitle('Daily new cases') # title of the chart

    ax = fig.add_subplot(111)
    # plot function to create 2 time series plots in a chart

    ax.plot(dictionary.Date, dictionary.Newcases, label=plot_A, linewidth=3)
    ax.plot(dictionary1.Date, dictionary1.Newcases,  label=plot_B, linewidth=3)

    # legend for 2 times series plots
    ax.legend() 
    ax.set_xlabel('Date') # define x axis label
    ax.set_ylabel('Cases per million people') # define y axis label
    return fig

def draw_des2_plot(filter, csv):
    """
    This function is to draw the plot of DES 2.
    """ 
    # labels = ['USA', 'Brazil', 'India', 'Mexico', 'Peru']
    # sizes = [31, 27, 21, 12, 9]

    labels = cp.death_rates(filter, csv)['location']
    sizes = cp.death_rates(filter, csv)['mortality_rate']
    plt.xkcd()

    plt.figure(1)
    fig = plt.gcf()
    DPI = fig.get_dpi()
    fig.set_size_inches(320 * 2 / float(DPI), 350 / float(DPI))

    fig.suptitle(f'5 {filter} rates by country')

    ax = fig.add_subplot(111)
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', normalize=True)
    ax.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.
    return fig

def draw_des3_plot(filter, csv):
    """
    This function is to draw the plot of DES 3.
    """ 
    objects = cp.fully_vaccinated_rate(filter, csv)['country']

    y_pos = np.arange(len(objects))
    performance = cp.fully_vaccinated_rate(filter, csv)['fvr']

    plt.xkcd()

    plt.figure(1)
    fig = plt.gcf()
    DPI = fig.get_dpi()
    fig.set_size_inches(320 * 2 / float(DPI), 350 / float(DPI))
    fig.suptitle('Percentage of people fully vaccinated by country')
    ax = fig.add_subplot(111)
    ax.barh(y_pos, performance, align='center', alpha=0.5)
    plt.yticks(y_pos, objects)
    ax.set_xlabel('Share of people fully vaccinated(%)')
    return fig