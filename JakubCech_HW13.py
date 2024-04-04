#Funkce č. 1 - kalkulačka
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

abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
       'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
       '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
       'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
       'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
       '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

#Funkce č. 2 - Ceasar cypher
def main2():
    new = []
    message = list(input("Enter your message without spaces: "))
    mode = str(input("Encrypt or decrypt? e/d: "))
    while True:
        try:
            number = abs(int(input("Cypher number: ")) % 27)
            break
        except ValueError:
            print("Zadej číslo!")

    if mode == "e":
        encrypt(message, number, new)

    elif mode == "d":
        decrypt(message, number, new)

    else:
        print("Zadej správný příkaz.")

def encrypt(message, number, new):
    for letter in message:
        x = int(abc.index(letter))
        new += abc[x + number]
    print(''.join(new))

def decrypt(message, number, new):
    for letter in message:
        x = int(abc.index(letter))
        new += abc[x - number]
    print(''.join(new))

main2()
