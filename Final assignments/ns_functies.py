def standaardtarief(afstandKM):
    if 50 > afstandKM > 0:
        return afstandKM * 0.80
    elif afstandKM >= 50:
        return afstandKM * 0.60 + 15
    else:
        tarief = 0
    return tarief


def ritprijs(leeftijd, weekendrit, afstandKM):
    tarief = standaardtarief(afstandKM)  # call on function to get price
    if leeftijd < 12 or leeftijd >= 65:
        res = tarief * 0.70
        if weekendrit:
            res = tarief * 0.65
    elif weekendrit:
        res = tarief * 0.60
    else:
        res = tarief
    return format(res, '.2f')


# User input
input_leeftijd = int(input('Wat is uw leeftijd?: '))
input_afstand = int(input('Hoeveel KM gaat u reizen?: '))
input_weekendrit = str(input('Gaat u in het weekend reizen? (Ja/Nee): ').lower())
if 'ja' == input_weekendrit:
    ticket = ritprijs(input_leeftijd, True, input_afstand)
    print(f'De reis gaat u {ticket} euro kosten.')
elif 'nee' == input_weekendrit:
    ticket = ritprijs(input_leeftijd, False, input_afstand)
    print(f'De reis gaat u {ticket} euro kosten.')
