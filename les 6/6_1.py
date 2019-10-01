def convert(celsius):
    celsius = int(celsius)
    fahrenheit = celsius * 1.8 + 32
    return fahrenheit


def table():
    print('{:^9} {:^6}'.format('F', 'C'))
    for c in range(-30, 41, 10):
        f = convert(c)
        print('{0:7.1f} {1:7.1f}'.format(f, c))

table()

