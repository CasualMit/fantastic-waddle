import os

aantal_kluizen = 12
kluis_nummers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']


#  function for the menu
def menu():
    while True:
        while True:
            try:
                menuopties = int(input('\n1: Hoeveel kluizen vrij \n2: Nieuwe kluis \n'
                               '3: Tussentijds openen \n4: Geef kluis terug\n'
                               '5: Exit \nVoer hier je keuze in: '))
            except:
                print('Voer een getal in(1-5)')
            else:
                break
        if menuopties == 1:
            toon_aantal_kluizen_vrij()
        elif menuopties == 2:
            nieuwe_kluis()
        elif menuopties == 3:
            kluis_openen()
        elif menuopties == 4:
            kluis_teruggeven()
        elif menuopties == 5:
            print('Exit')
            break
        else:
            print('Ongeldige invoer, voer een getal in(1-5)')


def toon_aantal_kluizen_vrij():  # function to show the free safes
    # check if the file is there with an if statement // if the file is there continue
    if os.path.isfile('kluizen.txt'):
        file = open('kluizen.txt', 'r')
        global kluizen
        kluizen = file.readlines()
        file.close()
    # if the file is not there, print an error message and quit the script
    else:
        print('Sorry er ging iets fout')
        exit()
    kluizen_bezet = 0
    for vrij in kluizen:
        if vrij:
            kluizen_bezet = kluizen_bezet + 1
    kluizen_vrij = aantal_kluizen - kluizen_bezet
    print(f'Op dit moment zijn er {kluizen_vrij} kluizen vrij')


def nieuwe_kluis():  # function to register a new safe
    if os.path.isfile('kluizen.txt'):
        file = open('kluizen.txt', 'r')
        global kluizen
        kluizen = file.readlines()
        file.close()
    else:
        print('Sorry er gaat iets fout')
        exit()
    #  this for loop is to check which safe is in use // if the safe is in use delete it from the variable.
    for kluis in kluizen:
        nummer = kluis.split(';')
        if nummer[0] in kluis_nummers:
            kluis_nummers.remove(nummer[0])
    if 12 >= len(kluis_nummers) > 0:
        print(f'Het nummer van je nieuwe kluis is {kluis_nummers[0]}')
        while True:
            toegangscode = str(input('Vul hier uw nieuwe 4-cijferige toegangscode in: '))
            if len(toegangscode) == 4:
                print('Uw kluis wordt is gesloten')
                break
            else:
                print('Voer minimaal 4 cijfers in.')
        file = open('kluizen.txt', 'a')
        file.write(f'\n{kluis_nummers[0]};{toegangscode}\n')
        file.close()
    else:
        print('Alle kluizen zijn in gebruik.')
        quit()


def kluis_openen():
    if os.path.isfile('kluizen.txt'):
        file = open('kluizen.txt', 'r')
        global kluizen
        kluizen = file.readlines()
        file.close()
    else:
        print('Sorry er gaat iets fout!')
        exit()
    goed_wachtwoord = 0
    while True:
        try:
            kluisnummer = int(input('Wat is uw kluisnummer?: '))
        except ValueError:  # note to self: kijk onderaan script voor info over valueerror
            print('Error, vul een correct getal in (1-12)')
        else:
            break
    toegangscode = str(input('Vul uw toegangscode in:'))
    for kluis in kluizen:
        if str(kluisnummer) + ';' + str(toegangscode) + '\n' == kluis:
            goed_wachtwoord = 1
    if goed_wachtwoord == 1:
        print('Uw kluis wordt geopened!')
    else:
        print('Uw toegangscode is incorrect.')


def kluis_teruggeven():
    if os.path.isfile('kluizen.txt'):
        file = open('kluizen.txt', 'r')
        global kluizen, kluisnummer
        kluizen = file.readlines()
        file.close()
    else:
        print('Sorry er gaat iets fout')
        exit()
    while True:
        try:
            kluisnummer = int(input('Wat is uw kluisnummer?:'))
        except ValueError:
            print('Error, vul een correct getal in (1-12)')
        else:
            break
    toegangscode = str(input('Vul uw toegangscode in:'))
    file = open('kluizen.txt', 'w')
    correct = 0
    for kluis in kluizen:
        if (str(kluisnummer) + ';' + str(toegangscode) + '\n') != kluis:
            file.write(kluis)
        if (str(kluisnummer) + ';' + str(toegangscode) + '\n') == kluis:
            correct = 1
    if correct == 0:
        print('U heeft de verkeerde toeganscode ingevoerd.')
    elif correct == 1:
        print('U heeft uw kluis succesvol teruggeven!')


menu()
