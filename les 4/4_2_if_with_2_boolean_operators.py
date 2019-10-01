# gather facts
age = input('Geef je leeftijd: ')
passport = input('Nederlands paspoort (ja/nee): ')

# compare age and check passport
if int(age) >= 18 and passport == 'ja':
    print('Gefelciteerd, je mag stemmen!')