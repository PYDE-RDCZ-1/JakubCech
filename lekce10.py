
import random
import funkce
import time



#import random

#def hod_kostkou():
#    pokracovat = True

#    while pokracovat == True:
#        print(random.randint(1, 6))
#        ano_ne = input("Chceš pokračovat? y/n")
#        if ano_ne == "n":
#            pokracovat = False

funkce.hod_kostkou()

#def vetsi_mensi():
#    if cislo_x > hadane_cislo:
#        print("Tvůj tip je nižší než x.")
#    elif cislo_x < hadane_cislo:
#        print("Tvůj tip je vyšší než x.")
#    else:
#        print("Bingo!")

pokusy = 0
pokracovat = True
cislo_x = int(random.randint(1, 100))

while pokracovat == True:
    pokusy += 1
    hadane_cislo = int(input("Zadej tip: "))
    vetsi_mensi()
    if cislo_x == hadane_cislo:
        pokracovat = False
        print(pokusy)

#def odpocet(cas):

#    for i in range (cas):
#        time.sleep(1)
#        print(cas - i)

delka_odpoctu = int(input("Zadej počet sekund pro odpočet."))

odpocet(delka_odpoctu)




