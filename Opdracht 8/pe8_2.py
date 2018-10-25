lijst = eval(input('Geef een lijst met minimaal 10 strings: '))

for word in lijst:
        if len(lijst) >= 10 and len(word) ==4:
            print(word)