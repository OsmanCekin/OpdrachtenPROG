file = open('C:/Users/Fener/PycharmProjects/Opdrachten/Opdracht 7/kaartnummers.txt', 'r')

regels = file.readlines()

file.close()

kaartnummers = []

for regel in regels:

    regel = regel.split(',')
    kaartnummers.append(int(regel[0]))


grootsteKaartnummer = max(kaartnummers)
regelGrootsteKaartnummer = kaartnummers.index(grootsteKaartnummer)+1

print('Deze file telt ' + str(len(kaartnummers)) + ' regels.')
print('Het grootste kaartnummer is: ' + str(grootsteKaartnummer) + ' en dat staat op regel ' + str(regelGrootsteKaartnummer))

