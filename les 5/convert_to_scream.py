def convert_to_scream(text):
    # A scream is all-caps and ends with an exclamation mark
    return text.upper() + '!'


message = input('Wat wil je schreeuwen?: ')

loud_message = convert_to_scream(message)

print(loud_message)
