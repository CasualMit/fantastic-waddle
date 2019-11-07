def loop():
    result = 0
    loops = 0
    while True:
        invoer = int(input('Geef een getal: '))
        if invoer == 0:
            break
        else:
            result = result + invoer
            loops += 1
    print(f'Er zijn {loops} getallen ingevoerd, de som is {result}')


loop()
