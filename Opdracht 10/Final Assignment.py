def inlezen_beginstation(stations):
    laatsteHalte = 'maastricht'
    invoerBeginstation = input('Wat is je beginstation?: ').lower()
    if invoerBeginstation == laatsteHalte:
        print(laatsteHalte + ' is de laatste halte. Vul een andere beginstation in.')
    elif invoerBeginstation in stations:
        return invoerBeginstation
    else:
        print('Deze trein komt niet in ' + invoerBeginstation)
    return inlezen_beginstation(stations)

def inlezen_eindstation(stations, beginstation):
    invoerEindstation = input('Wat is je eindstation?: ').lower()
    if invoerEindstation in stations:
        if is_eindstation_verder_dan_beginstation(stations.index(beginstation), stations.index(invoerEindstation)):
            return invoerEindstation
        else:
            print('Deze trein komt niet in ' + invoerEindstation)
    else: print('Station bestaat niet ' + invoerEindstation)
    return inlezen_eindstation(stations, beginstation)

def omroepen_reis(stations, beginstation, eindstation):
    indexEindstation = (stations.index(eindstation))
    indexBeginstation= (stations.index(beginstation))
    deHoeveelsteBeginstation = '\n' + 'Het beginstation ' + beginstation + ' is het ' + str(indexBeginstation + 1) + 'e station in het traject.'
    deHoeveelsteEindstation = 'Het eindstation ' + eindstation + ' is het ' + (str(indexEindstation + 1)) + 'e station in het traject.'
    afstandAantalStations = 'De afstand bedraagt ' + str(indexEindstation - indexBeginstation) + ' station(s)'
    prijsPerTreinhalte = int(5)
    prijsTreinKaartje = 'De prijs van het kaartje is ' + str((indexEindstation - indexBeginstation) * prijsPerTreinhalte) + ' euro.' + '\n'
    waarPersoonInstapt = 'Jij stapt in de trein in : ' + beginstation

    tussenStops = stations[(indexBeginstation + 1):indexEindstation]


    waarPersoonUitstapt = 'Jij stapt uit de trein in: ' + eindstation


    print(deHoeveelsteBeginstation)
    print(deHoeveelsteEindstation)
    print(afstandAantalStations)
    print(prijsTreinKaartje)
    print(waarPersoonInstapt)
    for stations in tussenStops:
        print(str('- ') + stations)
    print(waarPersoonUitstapt)


def is_eindstation_verder_dan_beginstation(indexBeginstation, indexEindstation):
    return indexBeginstation < indexEindstation




stations = ['schagen', 'heerhugowaard', 'alkmaar', 'castricum', 'zaandam', 'amsterdam sloterdijk', 'amsterdam centraal', 'amsterdam amstel', 'utrecht centraal', "'s-hertogenbosch", 'eindhoven', 'weert', 'roermond', 'sittard', 'maastricht']
beginstation = inlezen_beginstation(stations)
eindstation = inlezen_eindstation(stations, beginstation)
omroepen_reis(stations, beginstation, eindstation)