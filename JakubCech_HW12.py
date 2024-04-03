seznam = [("vejce", 10), ("chleba", 1), ("jablka", 4), ("mleko", 2), ("brambory", 8)]

prices = {
    "vejce": 5,
    "chleba": 30,
    "jablka": 7,
    "mleko": 20,
    "brambory": 6
}

total_price = 0

for index, (zbozi, mnozstvi) in enumerate(seznam):
    cena_zbozi = prices[zbozi]
    celkova_cena_zbozi = cena_zbozi * mnozstvi
    total_price += celkova_cena_zbozi

print(f"Celková cena nákupu je {total_price}. ")


