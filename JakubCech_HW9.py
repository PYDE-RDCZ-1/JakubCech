
def main():
    while True:
        try:
            a = float(input("Zadej číslo a: "))
            op = (input("Zadej operator: "))
            b = float(input("Zadej číslo b: "))
            break
        except ValueError:
            print("Zadejte správné hodnoty!")

    if op in ("+", "-", "*", "/"):
        if op == "+":
            print(a + b)
        elif op == "-":
            print(a - b)
        elif op == "*":
            print(a * b)
        elif op == "/" and b != 0:
            print(a / b)
        else:
            print("Nulou dělit nelze.")
    else:
        print("Špatný operátor.")



main()






