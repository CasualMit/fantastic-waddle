def kwadraten(grondgetallen):
    som = 0
    for number in grondgetallen:
        if number > 0:
            squared = number ** 2
            som = som + squared
    return som


print('het totaal is:', (kwadraten([4, 5, 3, -81])))


# OF

def kwadraten(grondgetallen):
    som = []
    for number in grondgetallen:
        if number > 0:
            som.append(number ** 2)
    return sum(som)


print('het totaal is:', (kwadraten([2, 4, 0, -81])))

