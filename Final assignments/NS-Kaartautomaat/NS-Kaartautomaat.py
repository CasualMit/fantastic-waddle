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
    beginstation_nummer = stations.index(beginstation) + 1
    eindstation_nummer = stations.index(eindstation) + 1
    afstand_stations = eindstation_nummer - beginstation_nummer
    prijs = afstand_stations * 5
    print(f'Het beginstation {beginstation} is het {beginstation_nummer}e station in het traject')
    print(f'Het eindstation {eindstation} is het {eindstation_nummer}e station in het traject')
    print(f'De afstand bedraagt {afstand_stations} station(s)')
    print(f'De prijs van het kaartje is {prijs} euro')
    print(f'Jij stapt in de trein in: {beginstation}')
    for i in range(beginstation_nummer, (eindstation_nummer - 1), 1):
        print(f' - {stations[i]}')
    print(f'Je stapt uit in: {eindstation}')


stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Amsterdam Sloterdijk', 'Amsterdam Centraal',
            'Amsterdam Amstel', 'Utrecht Centraal', '’s-Hertogenbosch', 'Eindhoven', 'Weert', 'Roermond', 'Sittard',
            'Maastricht']
beginstation = inlezen_beginstation(stations)
eindstation = inlezen_eindstation(stations, beginstation)
omroepen_reis(stations, beginstation, eindstation)