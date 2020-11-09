def format_number(value):
    try:
        value = float(value)
    except ValueError:
        return "Sorry, I need a numerical value"


    return '{}0'.format(value) 