cijferICOR = 7
cijferPROG = 6
cijferCSN = 6

gemiddelde = (cijferICOR + cijferPROG + cijferCSN) / 3
beloning = (cijferICOR * 30) + (cijferPROG * 30) + (cijferCSN * 30)

lijn = 'Mijn cijfers (gemiddeld een ' + str(gemiddelde) + ') leveren een beloning van $' + str(beloning) + ' op'

print(lijn)
