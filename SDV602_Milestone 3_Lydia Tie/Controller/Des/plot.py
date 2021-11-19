import sys   
sys.path.append(".")
import PySimpleGUI as sg
import View.Draw_plot as dp

def accept( event, values, window, func, figure_agg):
    keep_going = True

    if event == '-UPDATE-':
        csv = "test_data/owid-covid-data.csv"

        if figure_agg:
            dp.delete_figure_agg(figure_agg)

        if window.Title == "Daily new Covid cases":

            try:
                choiceA = values['-COMBO1-']
                choiceB = values['-COMBO2-']

                figure_agg = dp.draw_figure(window['-CANVAS-'].TKCanvas, func(choiceA, choiceB, csv), window['-CONTROLS-'].TKCanvas)
                
            except UnboundLocalError:
                sg.Popup("Please submit a CSV file.")
            except KeyError:
                sg.Popup("Please select a correct CSV file.")
            except IndexError:
                sg.Popup("Please choose countries to plot the chart.")
            except Exception as e:
                sg.Popup(e)

        elif window.Title == 'Death rates by country':
            try:
                choiceA = values['-COMBO3-']
                figure_agg = dp.draw_figure(window['-CANVAS-'].TKCanvas, func(choiceA, csv), window['-CONTROLS-'].TKCanvas)
            except UnboundLocalError:
                sg.Popup("Please submit a CSV file.")
            except KeyError:
                sg.Popup("Please select a correct CSV file.")
            except IndexError:
                sg.Popup("Please choose countries to plot the chart.")
            except Exception as e:
                sg.Popup(e)
        
        elif window.Title == 'Fully Vaccinated rates by country':
            try:
                choiceA = values['-COMBO3-']
                figure_agg = dp.draw_figure(window['-CANVAS-'].TKCanvas, func(choiceA, csv), window['-CONTROLS-'].TKCanvas)
            except UnboundLocalError:
                sg.Popup("Please submit a CSV file.")
            except KeyError:
                sg.Popup("Please select a correct CSV file.")
            except IndexError:
                sg.Popup("Please choose countries to plot the chart.")
            except Exception as e:
                sg.Popup(e)

        else:
            figure_agg = None
        

    return keep_going, figure_agg
    
    
