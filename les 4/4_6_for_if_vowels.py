string = 'Guido van Rossum heeft programmeertaal Python bedacht.'
vowels = 'aeiouAEIOU'
for letters in string:
    if letters in vowels:
        print(letters)