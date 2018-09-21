cijferICOR = 7
cijferPROG = 6
cijferCSN = 6

gemiddelde = ((cijferICOR + cijferPROG + cijferCSN) / 3)
beloning = ((cijferICOR * 30) + (cijferPROG * 30) + (cijferCSN * 30))

overzicht = ('Mijn gemiddelde is ') + str(gemiddelde)
overzicht2 = (' en ik krijg ') + str(beloning)

print((overzicht) + (overzicht2))