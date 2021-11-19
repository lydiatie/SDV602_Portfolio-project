import sys 
sys.path.append(".")
from Model.user_manager import UserManager


def accept( event, values, window):
    keep_going = True
    if event == '-SEND-':
        a_user_manager = UserManager()
        msg = values['-MSG-']
        message_result = a_user_manager.send_chat(msg)
        window['-MSG-'].update("")
        
        print(f'{message_result}')

    return keep_going
