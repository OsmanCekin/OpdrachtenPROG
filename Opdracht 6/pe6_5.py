def kwadraten_som(grondgetallen):
    totaal = 0
    for x in grondgetallen:
        if x >= 0:
            totaal = totaal + x**2
    return totaal

lijst = [4, 5, 3, -81]
print(kwadraten_som(lijst))