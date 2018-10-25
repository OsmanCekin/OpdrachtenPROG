def gemiddelde():

    zin = input('Geef een zin:  ')
    optelling = 0
    for ch in zin.split():
        character = len(ch)
        optelling = optelling + character

    gemiddelde = optelling / len(zin.split())
    print(gemiddelde)

print(gemiddelde())