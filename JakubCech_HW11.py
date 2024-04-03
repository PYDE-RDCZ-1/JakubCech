abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
       'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
       'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
       'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def main():
    new = []
    message = list(input("Enter your message: "))
    mode = str(input("Encrypt or decrypt? e/d: "))
    number = abs(int(input("Cypher number: ")) % 27)

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