#def zadej_vek():
#    while True:
#        try:
#            vek = int(input("Zadej věk: "))
#            return vek
#        except ValueError:
#            print("Neplatné zadání. Zadej celé číslo.")
#
#def main():
#    vek = zadej_vek()
#    print("Váš věk je:", vek)
#
#main()

#def kalkulacka():
#    while True:
#        print("Vyberte operaci:")
#        print("1. Sčítání")
#        print("2. Odčítání")
#        print("3. Násobení")
#        print("4. Dělení")
#        print("5. Konec")
#
#        volba = input("Zadej číslo operace: ")
#
#        if volba in ("1", "2", "3", "4"):
#            try:
#                cislo1 = float(input("Zadej první číslo: "))
#                cislo2 = float(input("Zadej druhé číslo: "))
#                if volba == "1":
#                    print("Výsledek je: ", scitani(cislo1, cislo2))
#                elif volba == "2":
#                    print("Výsledek je: ", odcitani(cislo1, cislo2))
#                elif volba == "3":
#                    print("Výsledek je: ", nasobeni(cislo1, cislo2))
#                elif volba == "4":
#                    print("Výsledek je: ", deleni(cislo1, cislo2))
#            except (ValueError, ZeroDivisionError):
#                print("Chyba: Zadejte platné čísla.")
#        elif volba == "5":
#            print("Konec programu.")
#            break
#        else:
#            print("Chyba, nesprávná volba.")
#
#def scitani(cislo1, cislo2):
#    vysledek = cislo1 + cislo2
#    return vysledek
#
#def odcitani(cislo1, cislo2):
#    vysledek = cislo1 - cislo2
#    return vysledek
#
#def nasobeni(cislo1, cislo2):
#    vysledek = cislo1 * cislo2
#    return vysledek
#
#def deleni(cislo1, cislo2):
#    vysledek = cislo1 / cislo2
#    return vysledek
#
#kalkulacka()

def ziskej_vek():
    while True:
        try:
            vek = int(input("Zadej věk: "))
            return vek
        except ValueError:
            print("Zadej celé číslo!")


def main():
    vek = ziskej_vek()
    print("Vask vek je:", vek)


main()