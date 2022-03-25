#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 15:09:32 2022

@author: kamilla
"""

#DATA110 Obligatorisk hovedinnleveringsoppgave 1
#Hovedinnlevering 1

##Oppgave 1

print("oppgave 1")
import math

def pi(d = 2):
    """Funksjon som skriver pi med oppgitt antall desimaler"""
    decimals = d
    if d > 48:
        print("Math.pi gir ikke mer enn 48 desimaler for tallet pi")
        print("{:.{}f}".format(math.pi, 48))
    else:
        print(f"pi med {decimals} desimaler")
        print("{:.{}f}".format(math.pi, decimals))
    
pi(16)
print("\n")
pi(100)
print("\n")
print("\n")



##Oppgave 2

print("oppgave 2")
### F = 1.8C + 32
### C = (x - 32) / 1.8
def temperaturKonvertering(x, temperatur = "C"):
    """Funksjon som konventerer mellom Celsius og Fahrenheit"""
    if temperatur == "C" or temperatur == "c":
        F = (x * 1.8) + 32
        print(f"{x} Celsuis er {F} Fahrenheit")
    elif temperatur == "F" or temperatur == "f":
        C = (x - 32) / 1.8
        print(f"{x} Fahrenheit er {C} Celsius")
    else:
        print("Temperatur må være i Celsius eller Fahrenheit")

temperaturKonvertering(34, "F")
temperaturKonvertering(34)
print("\n")


##Oppgave 3

print("oppgave 3a, 3b og 3c")
print("\n")
saldo = 500
rentesats = 0.01
renteoppgjør = 0
if saldo >= 1000000:
    rentesats = 0.02
else:
    rentesats = 0.01

def innskudd(kr):
    global saldo
    saldo = saldo + kr 
    print(f"saldo er {saldo} kr etter innskudd av {kr} kr")

def uttak(kr):
    global saldo
    if saldo - kr >= 0:
        saldo = saldo - kr 
        print(f" Din saldo er {saldo} kr etter uttak av {kr} kr")
    elif saldo - kr < 0:
        print("Ikke dekning")
        

def beregnerente():
    global saldo
    global rentesats
    if saldo < 1000000:
        rentesats = 0.01
    elif saldo >= 1000000:
        rentesats = 0.02
    print(f" Din saldo er {saldo} derfor er rentesatsen {rentesats}%")
    

def årligrenteoppgjør():
    global saldo
    global rentesats
    global renteoppgjør
    if saldo < 1000000:
        rentesats = 0.01
    elif saldo >= 1000000:
        rentesats = 0.02
    renteoppgjør = saldo + (saldo * rentesats)
    print(f"Din saldo var {saldo}, derfor har du {rentesats}% rente. Etter årsoppgjøret er din nye saldo {renteoppgjør}")
    saldo = renteoppgjør

endringer_saldo = []

def velg ():
    print("Dine valg i banken er:")
    print("1 - Vis saldo")
    print("2 - Innskudd")
    print("3 - Uttak")
    print("4 - Renteoppgjør")
    print("5 - Tre siste endringer i saldoen")
    global saldo
    global endringer_saldo
    handling = int(input("Velg handling:"))
    if handling == 1:
        print(f"Saldo: {saldo}")
    elif handling == 2:
        kr_inn = int(input("Beløp:"))
        innskudd(kr_inn)
        inn = str(f"+{kr_inn}")
        endringer_saldo.append(inn)
        if saldo >= 1000000:
            print("Gratulerer, du får bonusrente")
    elif handling == 3:
        kr_ut = int(input("Beløp:"))
        uttak(kr_ut)
        ut = str(f"-{kr_ut}")
        endringer_saldo.append(ut)            
    elif handling == 4:
        beregnerente()
    elif handling == 5:
        if len(endringer_saldo) < 3:
            print("Det er mindre enn 3 endringer i din saldo")
            print("Dette er dine siste endringer")
            for verdi in endringer_saldo:
                print(verdi)
        elif len(endringer_saldo) >= 3:
            print("Det er 3 eller mer endringer i din saldo")
            print("Dette er dine 3 siste endringer")
            for verdi in range(-1, -4, -1):
                print(endringer_saldo[verdi])    
    elif handling != range(1,5):
        print("Du må velge handling 1 - 5 ")
        velg()
    print("\n")
    

    
velg()
velg()
velg()
velg()
velg()



