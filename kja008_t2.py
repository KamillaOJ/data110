#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 19:50:14 2022

@author: kamilla
"""

#DATA110 Obligatorisk innleveringsoppgave 2
#Temainnlevering 2

import math
import random

##Oppgave 1
print("oppgave 1")
print("Dette programmet regner ut arealet av en sirkel. Du må bare skrive inn radius")
radius = float(input("Radius:"))
pi = math.pi
print(f"Arealet til en sirkel med radius {radius} er {pi*(radius**2):.3f}")
print("\n")
print("\n")

##Oppgave 2
print("oppgave 2")
setning = input("Skriv en setning:")
lengde = len(setning.replace(" ", ""))
gjett = int(input("gjett hvor mange bokstaver det er i setningen:"))
if gjett == lengde:
    print("Det er riktig!")
else:
    print("Det er feil!")
print("\n")
print("\n")



##Oppgave 3
print("oppgave 3")

tall = str(input("Gi meg et tall:"))
tall_rand = tall + str(random.randint(0,9))
tall = int(tall)
tall_rand = int(tall_rand)
dele_rand = tall_rand / tall
print(f"{tall_rand}/{tall} = {dele_rand:.2f}")







