
def accept( event, values, window):
    keep_going = True
    if event == 'Send':
        msg = values['-MSG-'].rstrip()
        print(f'{msg}')
    return keep_going
