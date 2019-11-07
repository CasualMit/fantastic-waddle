def ticker():
    file = open('ticker.txt', 'r')
    inhoud = file.readlines()
    file.close()
    dictionary = dict()
    for line in inhoud:
        temp = line.split(':')
        dictionary[temp[0]] = temp[1]
    return dictionary


def res():
    dictionary = ticker()
    bedrijfsNaam = str(input('Enter company name: ').upper())
    for key, value in dictionary.items():
        if key == bedrijfsNaam:
            result = value
            print(f'Ticker symbol: {result}')
            break
        else:
            print('Please give a valid company name')
            break
    tickerNaam = str(input('Enter Ticker symbol: ').upper())
    for key, value in dictionary.items():
        if value == tickerNaam:
            result = key
            print(f'Company name: {result}')
            break
        else:
            print('Please give a valid ticker symbol')
            break


res()
