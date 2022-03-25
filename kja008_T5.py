#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 18:59:23 2022

@author: kamilla
"""

#DATA110 Obligatorisk innleveringsoppgave 5
#Temainnlevering 5

##Oppgave 1
print("oppgave 1")

def antallVokaler(t):
    vokaler = ["a", "e", "i", "o", "u", "y", "æ", "ø", "å"]
    sum_vokaler = 0
    for vokal in vokaler:
        lengde_tekst = t.count(vokal)
        sum_vokaler = sum_vokaler + lengde_tekst
    print(sum_vokaler)

antallVokaler("Her er det 6 vokaler")    
print("\n")


##Oppgave 2
print("oppgave 2")

TV =     \
'''
Tulleveien Velforening
leder: Kari
kasserer: Ole
IT-ansvarlig: Liv
parkeringsansvarlig: Kari
arrangementsansvarlig: Liv
hagekonsulent: Kari
brannansvarlig: Kari
'''

def verv(navn):
    verve_liste = []
    navn_plassering = TV.find(navn)
    if navn_plassering == -1: return navn + "finnes ikke"
    linjer = TV.split("\n")
    linjer[:] = (value for value in linjer if value != "")
    for linje in linjer:
        if navn in linje:
            plassering = linje.find(navn) -2
            type_verv = (linje[:plassering])
            verve_liste.append(type_verv)
    print(f"{navn} har følgende verv i Tulleveien velforening:")
    print(", ".join(verve_liste))
    print("\n")
    
            
     
verv("Liv")
verv("Kari")







