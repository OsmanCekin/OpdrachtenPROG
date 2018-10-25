def standaardprijs(afstandKM):
    vastbedrag = 15
    korteAfstandPrijsKM = 0.80
    langeAfstandPrijsKM = 0.60
    maxKM = 50
    ritprijs = 0
    if afstandKM <= 0:
        return '0'
    if afstandKM >= maxKM:
        ritprijs = (langeAfstandPrijsKM * afstandKM) + vastbedrag
    else:
        ritprijs = (korteAfstandPrijsKM * afstandKM) + vastbedrag
    return ritprijs
afstandKM = int(input('Hoeveel KM reist u?: '))
lijn = ('U betaald voor uw reis ' + str(standaardprijs(afstandKM)) + ' Euro')
print(lijn)

def ritprijs(leeftijd:int, weekendrit:bool, afstandkm:int):
    prijs=standaardprijs(afstandkm)

    maxLeeftijdKind = 12
    maxLeeftijdVol = 65
    leeftijdsKorting = False

    oudkindkorting = 0.70     #30% korting voor ouderen en kinderen met werkdagen
    weekendKorting = 0.65     #35% korting voor ouderen en kinderen in het weekend
    weekendNormaal = 0.60     #40% korting voor normale leeftijden in het weekend

    if leeftijd < maxLeeftijdKind or leeftijd >= maxLeeftijdVol:
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
leeftijd = int(input('Wat is uw leeftijd?: '))
print('Uw nieuwe uitgerekende prijs: ' + str(ritprijs(leeftijd, True, afstandKM))) #weekendrit staat aan en wordt uitgerekend

leeftijd= (11, 12, 64, 65)
afstandkm= (12, 40, 60)
for leeftijden in leeftijd:
    for afstand in afstandkm:
        print(str(leeftijd) + ' Jaar oud | ' + str(afstand) + 'KM | Weekend | $' + str(ritprijs(leeftijden, True, afstand)))

        print(str(leeftijd) + ' Jaar oud | ' + str(afstand) + 'KM | Week | $' + str(ritprijs(leeftijden, False, afstand)))
