def zadej_vek():
    while True:
        try:
            vek = int(input("Zadej věk: "))
            return vek
        except ValueError:
            print("Neplatné zadání. Zadej celé číslo.")

def main():
    vek = zadej_vek()
    print("Váš věk je:", vek)

main()