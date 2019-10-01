def lang_genoeg(lengte):
    if int(lengte) >= 120:
        return(print('Je bent lang genoeg voor de attractie!'))
    else:
        return(print('Sorry, je bent te klein!'))


lengte = input('Vul hier je lengte in centimeters in: ')

lang_genoeg(lengte)
