def standaardtarief(afstandKM):
    if 50 > afstandKM > 0:
        return int(afstandKM) * 0.80
    elif afstandKM >= 50:
        return int(afstandKM) * 0.60 + 15
    return 0


def ritprijs(leeftijd, weekendrit, afstandKM):
    tarief = standaardtarief(afstandKM)  # call on function to get price
    leeftijd = int(leeftijd)  # make it an int to not repeat it
    if leeftijd < 12 or leeftijd >= 65:
        res = tarief * 0.70
        if weekendrit:
            res = tarief * 0.65
    elif weekendrit:
        res = tarief * 0.60
    else:
        res = tarief
    return res


test = ((11, 12, 64, 65), (10, 100, -69, 0))
for leeftijd in test[0]:
    for afstand in test[1]:
        for weekendrit in (True, False):
            reiskosten = ritprijs(leeftijd, weekendrit, afstand)
            print(f'leeftijd= {leeftijd} // afstand {afstand} // weekendrit? {weekendrit} // kosten {reiskosten}')
    print(' ')


