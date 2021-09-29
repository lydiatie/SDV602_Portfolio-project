import sys   
sys.path.append(".")
import PySimpleGUI as sg
import View.Draw_plot as dp



def accept( event, values, window, func):
    keep_going = True

    if event == '-UPDATE-':

        
        if window.Title == "Daily new Covid cases":

            try:
                choiceA = values['-COMBO1-']
                choiceB = values['-COMBO2-']

                figure_agg = dp.draw_figure(window['-CANVAS-'].TKCanvas, func(choiceA, choiceB, values["-IN-"]), window['-CONTROLS-'].TKCanvas)
                
            except UnboundLocalError:
                sg.Popup("Please submit a CSV file.")
            except KeyError:
                sg.Popup("Please select a correct CSV file.")
            except IndexError:
                sg.Popup("Please choose countries to plot the chart.")
            except Exception as e:
                sg.Popup(e)

        if window.Title == 'Death rates by country':
            try:
                choiceA = values['-COMBO3-']
                figure_agg = dp.draw_figure(window['-CANVAS-'].TKCanvas, func(choiceA, values["-IN-"]), window['-CONTROLS-'].TKCanvas)
            except UnboundLocalError:
                sg.Popup("Please submit a CSV file.")
            except KeyError:
                sg.Popup("Please select a correct CSV file.")
            except IndexError:
                sg.Popup("Please choose countries to plot the chart.")
            except Exception as e:
                sg.Popup(e)
        
        if window.Title == 'Fully Vaccinated rates by country':
            try:
                choiceA = values['-COMBO3-']
                figure_agg = dp.draw_figure(window['-CANVAS-'].TKCanvas, func(choiceA, values["-IN-"]), window['-CONTROLS-'].TKCanvas)
            except UnboundLocalError:
                sg.Popup("Please submit a CSV file.")
            except KeyError:
                sg.Popup("Please select a correct CSV file.")
            except IndexError:
                sg.Popup("Please choose countries to plot the chart.")
            except Exception as e:
                sg.Popup(e)
    return keep_going
    
    
