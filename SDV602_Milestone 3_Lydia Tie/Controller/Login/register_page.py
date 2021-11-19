from View.Register import register_view

def accept(event, value, window):
    keep_going = True
    
    if event == 'Register':

        window.close()
        register_view()
        keep_going = False

    return keep_going