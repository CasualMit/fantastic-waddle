cijferICOR = 8
cijferPROG = 7
cijferCSN = 6

vakken = cijferICOR + cijferPROG + cijferCSN

gemiddelde = vakken / 3

beloning = vakken * 30

overzicht = 'Mijn cijfers gemiddeld een ' + str(gemiddelde) + ' leveren een beloning van € ' + str(beloning) + ' op!'
print(overzicht)