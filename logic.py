def format_number(value):

    # We discard non-numbers
    try:
        value = float(value)
    except ValueError:
        return "Sorry, I need a numerical value"

    # Now we deal with the decimal parts
    return format(value, ",.2f").replace(',', ' ')