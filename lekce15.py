try:
    with open("example.txt", 'r') as soubor:
        #text je jeden velký string
        obsah = soubor.read()

        #rozdělíme string a vznikne list
        slova_seznam = obsah.split()
        print(slova_seznam)
        print(len(slova_seznam))

        #vytvoříme z listu set (zbavíme se duplicity)
        unikatni_slova = set(slova_seznam)
        print(unikatni_slova)

        #vytvoříme dictionary
        slova_dict = dict()
        for slovo in slova_seznam:
            if slovo in slova_dict:
                slova_dict[slovo] += 1
            else:
                slova_dict[slovo] = 1
        nejcastejsi_slovo = max(slova_dict, key=slova_dict.get)
        nejcastejsi_slovo_pocet = slova_dict[nejcastejsi_slovo]
        print(nejcastejsi_slovo)
        print(nejcastejsi_slovo_pocet)


    print(slova_dict)


except FileNotFoundError:
    print("Soubor nebyl nalezen.")
except PermissionError:
    print("Nemáte povolení ke čtení souboru.")