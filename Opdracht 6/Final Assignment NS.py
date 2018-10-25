def standaardprijs(afstandkm):
    langeAfstandPrijsPerKm = 0.60
    korteAfstandPrijsPerKm = 0.80
    prijsPerKm = korteAfstandPrijsPerKm
    maxKm = 50
    vastBedrag = 15
    ritprijs = 0
    if afstandkm >= maxKm:
        prijsPerKm = langeAfstandPrijsPerKm
        ritprijs = prijsPerKm*afstandkm + vastBedrag
    else:
        ritprijs = prijsPerKm*afstandkm

    return ritprijs
afstandkm = int(input(('Hoeveel km reist u? ')))
test=input('U betaald voor uw reis $' + str(standaardprijs(afstandkm)))
print(test)


def ritprijs(leeftijd:int, weekendrit:bool, afstandkm:int):
    prijs=standaardprijs(afstandkm)

    maxLeeftijdKind = 12
    maxLeeftijdVol = 65
    leeftijdsKorting = False

    oudkindkorting = 0.70     #30% korting voor ouderen en kinderen met werkdagen
    weekendKorting = 0.65     #35% korting voor ouderen en kinderen in het weekend
    weekendNormaal = 0.60     #40% korting voor normale leeftijden in het weekend

    heeftRechtOpLeeftijdsKorting = leeftijd < maxLeeftijdKind or leeftijd >= maxLeeftijdVol
    if heeftRechtOpLeeftijdsKorting:
        leeftijdsKorting = True

    if weekendrit:
        if leeftijdsKorting:
            prijs=prijs*weekendKorting
        else:
            prijs=prijs*weekendNormaal
    else:
        if leeftijdsKorting:
            prijs=prijs*oudkindkorting

    return round(prijs, 2)



leeftijd=int(input('Wat is uw leeftijd? '))
# weekendrit=False or True
# print(ritprijs())
print(ritprijs(leeftijd, True, 20))

leeftijd= (11, 12, 64, 65)
afstandkm= (12, 40, 60)

for leeftijden in leeftijd:
    for afstand in afstandkm:
        print(str(leeftijd) + ' Jaar oud | ' + str(afstand) + 'KM | Weekend | $' + str(ritprijs(leeftijden, True, afstand)))

        print(str(leeftijd) + ' Jaar oud | ' + str(afstand) + 'KM | Week | $' + str(ritprijs(leeftijden, False, afstand)))