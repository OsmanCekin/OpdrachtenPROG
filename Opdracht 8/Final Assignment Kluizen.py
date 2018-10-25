import random


def kluis_aanmaken():
    bestand = open("C:/Users/Fener/PycharmProjects/Opdrachten/Opdracht 8/kluizen.txt", "r")
    regels = bestand.readlines()
    kluizen = []
    for regel in regels:
        kluis = regel.strip().split('.')
        kluizen.append(int(kluis[0]))
        bestand.close()
    if len(kluizen) <12:
        if len(kluizen) <= 0:
            kluisnummer = 1
        else:
            kluisnummer = kluizen[-1] + 1

        print()
        print("uw kluisnummer is", kluisnummer)
        pincode = random.randint(1000, 9999)
        print("uw code is", pincode)
        print()
        bestand = open("C:/Users/Fener/PycharmProjects/Opdrachten/Opdracht 8/kluizen.txt", "a")
        bestand.write(str(kluisnummer))
        bestand.write(".")
        bestand.write(str(pincode))
        bestand.write("\n")
        bestand.close()
    else:
        print("er zijn geen kluizen meer beschikbaar")

def openen_van_kluis():
    kluisnummer = input("wat is uw kluisnummer")
    ingevoerd_ww = input("wat is uw code")
    bestand = open("C:/Users/Fener/PycharmProjects/Opdrachten/Opdracht 8/kluizen.txt", "r")
    regels = bestand.readlines()
    pincode = []

    for regel in regels:
        kluis = regel.strip().split('.')
        pincode.append(int(kluis[1]))
        bestand.close()
    if int(ingevoerd_ww) in pincode:
        kluisnummer = pincode.index(int(ingevoerd_ww)) + 1
        print()
        print("kluisnummer", kluisnummer, "is geopend voor u")
        print()
    else:
        print()
        print("ongeldige code")
        print()

def lees_kluizen():
    bestand = open("C:/Users/Fener/PycharmProjects/Opdrachten/Opdracht 8/kluizen.txt", "r")
    regels = bestand.readlines()
    kluizen = []
    for regel in regels:
        kluis = regel.strip().split('.')
        kluizen.append(int(kluis[0]))
        bestand.close()
    print()
    print("Er zijn", 12-len(kluizen), "kluizen vrij")
    print()
    return kluizen


while True:

    antwoord =int(input("wat wilt u doen\n" \
          "1: Ik wil weten hoeveel kluizen nog vrij zijn\n" \
          "2: Ik wil een nieuwe kluis\n" \
          "3: Ik wil even iets uit mijn kluis halen\n" \
          "4: Ik wil mijn kluis teruggeven\n" \
          "5: Ik wil het programma beëindigen\n" \
          " "))

    if antwoord == 1:
        lees_kluizen()
    elif antwoord == 2:
        kluis_aanmaken()
    elif antwoord == 3:
        openen_van_kluis()
    elif antwoord == 4:
        print()
        print("ik geef geen kluizen terug")
        print()
    elif antwoord == 5:
        print ("Programma wordt beëindigd")

        break
    else:
        print()
        print("ongeldig probeer opnieuw")
        print()