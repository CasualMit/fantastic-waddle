price = 4356


def priceprogram():
    while True:
        try:
            persons = int(input('Hoeveel mensen gaan er mee? '))
            if persons < 0:
                raise Exception
            elif persons == 0:
                raise ZeroDivisionError
            else:
                break
        except ZeroDivisionError:
            print('Je kan de kosten niet delen door 0 personen')
        except ValueError:
            print('Voer een getal in.')
        except Exception:
            print('Je kan geen negatief getal invoeren.')
        except:
            print('Er is iets misgegaan neem contact op met uw beheerder')
    result = price / persons
    print(f'De kosten zijn €{result} per persoon')


priceprogram()

