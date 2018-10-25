gebruikerLengte = int(input('Hoe lang ben je?: '))

def lang_genoeg(lengte):
    if lengte >= 120:
        return 'Je bent lang genoeg'
    else:
        return 'Sorry, je bent te klein'
print(lang_genoeg(gebruikerLengte))
