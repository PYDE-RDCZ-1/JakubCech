import random
import time
import math

def odpocet(cas):
    for i in range (cas):
        time.sleep(1)
        print(cas - i)


def vetsi_mensi():
    if cislo_x > hadane_cislo:
        print("Tvůj tip je nižší než x.")
    elif cislo_x < hadane_cislo:
        print("Tvůj tip je vyšší než x.")
    else:
        print("Bingo!")


def hod_kostkou():
    pokracovat = True
    while pokracovat == True:
        print(random.randint(1, 6))
        ano_ne = input("Chceš pokračovat? y/n")
        if ano_ne == "n":
            break


def obvod_obsah(polomer):
    obvod = 2 * math.pi * polomer
    obsah = math.pi * polomer ** 2
    return obvod, obsah