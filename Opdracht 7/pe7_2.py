def kaartnummer():
    file = open('C:/Users/Fener/PycharmProjects/Opdrachten/Opdracht 7/kaartnummers.txt')

    kaartlees = file.readlines()

    file.close()


    for name in kaartlees:
        fl=name.split(',')
        print('{} heeft kaartnummer: {}'.format(fl[1].strip(), fl[0]))

kaartnummer()