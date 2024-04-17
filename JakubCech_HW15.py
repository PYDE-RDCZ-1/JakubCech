cesta_k_souboru = "nakupni seznam.txt"

seznam = ["apple", "banana", "grape", "orange", "kiwi", "pineapple", "strawberry", "melon"]

with open(cesta_k_souboru, 'w') as soubor:
    for item in seznam:
        soubor.write(item + " ")