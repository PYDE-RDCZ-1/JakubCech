def bmi_calculate(weight, height):

    bmi = weight / (height ** 2)
    return bmi

def bmi_level(bmi):
    if bmi < 18.5:
        return "Podvaha"
    elif bmi < 25:
        return "Normalni"
    elif bmi < 30:
        return "Nadvaha"
    else:
        return "Obezita"

def main():
    weight = float(input("Zadej váhu v kg: "))
    height = (float(input("Zadej výšku v cm: "))) / 100

    bmi = bmi_calculate(weight, height)

    bmi_cathegory = bmi_level(bmi)

    print(f"Vaše BMI je {bmi}.")
    print(f"Spadáte do kategorie {bmi_cathegory}.")

if __name__ == "__main__":
    main()