def seizoen(maand):

    if maand >= 9 and maand <=11:
        print('herfst')
    elif maand >= 6 and maand <= 8:
        print('zomer')
    elif maand >= 3 and maand <= 5:
        print('lente')
    else:
        print('winter')

seizoen(maand = int(input('Geef het nummer van de maand op: ')))