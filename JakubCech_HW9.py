def calc(a, b, op):

    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/" and b != 0:
        return a / b
    else:
        return("Nulou dělit nelze.")


a = float(input("Zadej číslo a: "))
op = input("Zadej operator: ")
b = float(input("Zadej číslo b: "))

print(calc(a, b, op))






