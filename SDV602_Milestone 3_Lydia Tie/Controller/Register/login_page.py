from View.Login import login_view

def accept( event, value, window):
    keep_going = True
    if event == '-LOGIN-':
        window.close()
        login_view()
        keep_going = False
    return keep_going
