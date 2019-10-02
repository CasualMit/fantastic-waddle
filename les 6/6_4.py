def strftime():
    import datetime
    vandaag = datetime.datetime.today()
    s = vandaag.strftime("%a %d %b %Y, %H:%M:%S")
    return (s)

def checkpoint():
    file = open('hardlopers.txt', 'a+')
    current = strftime()
    while True:
        name = input('Naam van hardloper: ')
        if name == '':
            return
        file.write((f'{current}, {name} \n'))


checkpoint()
