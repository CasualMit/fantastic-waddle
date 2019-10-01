def strftime():
    import datetime
    vandaag = datetime.datetime.today()
    s = vandaag.strftime("%a %d %b %Y, %H:%M:%S")
    return (s)

def checkpoint(name):
    file = open('hardlopers.txt', 'a+')
    name = name
    current = strftime()
    file.write((f'{current}, {name} \n'))
    return


checkpoint(input('Naam van hardloper: '))
