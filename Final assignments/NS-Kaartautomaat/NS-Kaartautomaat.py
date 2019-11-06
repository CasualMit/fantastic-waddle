def inlezen_beginstation(stations):
    while True:
        user_input = str(input('Wat is je begin station? '))
        if user_input in stations and user_input != stations[-1]:
            return user_input
        else:
            print(f'Deze trein komt niet in {user_input}.')


def inlezen_eindstation(stations, beginstation):
    while True:
        user_input = str(input('Wat is je eindstation?: '))
        if user_input in stations and stations.index(user_input) > stations.index(beginstation):
            return user_input
        else:
            print(f'Deze trein komt niet in {user_input}.')


def omroepen_reis(stations, beginstation, eindstation):
    beginstationNummer = stations.index(beginstation) + 1
    eindstationNummer = stations.index(eindstation) + 1
    afstandStations = eindstationNummer - beginstationNummer
    prijs = afstandStations * 5
    print(f'Het beginstation {beginstation} is het {beginstationNummer}e station in het traject')
    print(f'Het eindstation {eindstation} is het {eindstationNummer}e station in het traject')
    print(f'De afstand bedraagt {afstandStations} station(s)')
    print(f'De prijs van het kaartje is {prijs} euro')
    print(f'Jij stapt in de trein in: {beginstation}')
    for i in range(beginstationNummer, (eindstationNummer - 1), 1):
        print(' - {}'.format(stations[i]))
    print('Je stapt uit in: {}'.format(eindstation))


stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Amsterdam Sloterdijk', 'Amsterdam Centraal',
            'Amsterdam Amstel', 'Utrecht Centraal', '’s-Hertogenbosch', 'Eindhoven', 'Weert', 'Roermond', 'Sittard',
            'Maastricht']
beginstation = inlezen_beginstation(stations)
eindstation = inlezen_eindstation(stations, beginstation)
omroepen_reis(stations, beginstation, eindstation)