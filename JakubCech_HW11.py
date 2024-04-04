abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
       'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
       '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
       'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
       'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
       '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

def main():
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

main()