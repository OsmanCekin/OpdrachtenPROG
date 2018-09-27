lengte = input('Hoe lang (cm) ben je? ')

def lang_genoeg(lengte):
    if eval(lengte) >= 120:
        print('Je bent lang genoeg!')
    else:
        print('Sorry je bent te klein')
    return lengte
print(lang_genoeg(lengte))