def seizoen(maand):
    wintermaanden = [12, 1, 2]
    lentemaanden = [3, 4, 5]
    zomermaanden = [6, 7, 8]
    herftsmaanden = [9, 10, 11]

    if maand in wintermaanden:
        return 'Winter'
    elif maand in lentemaanden:
        return 'Lente'
    elif maand in zomermaanden:
        return 'Zomer'
    elif maand in herftsmaanden:
        return 'Herfst'


print(seizoen(9))
