def convert(celsius):
    somFahrenheit = celsius * 1.8 + 32
    return somFahrenheit

def table(start, eind, stap):
    print('{:6} {:6}'.format('  F','   C'))

    for i in range(start, eind + stap, stap):
        print('{:6} {:6}'. format(convert(i), i))

table(-30, 40, 10)