
def accept( event, values):
    keep_going = True
    if event == 'Send':
        msg = values['-MSG-'].rstrip()
        print(f'{msg}')
    return keep_going
