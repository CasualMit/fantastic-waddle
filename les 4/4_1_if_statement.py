# gather facts
score = input('Geef je score: ')
# compare score with minimal requirements and print result
if int(score) > 15:
    print('Gefeliciteerd!')
    print('Met een score van ' + score + ' ben je geslaagd!')

# Mocht deze hier direct onder de 'if' staan wordt hij altijd geprint
# print('Met een score van ' + score + ' ben je geslaagd!')