#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 11:32:25 2022

@author: kamilla
"""


#DATA110 Obligatorisk innleveringsoppgave 6
#Temainnlevering 6

import os


##Oppgave 1
print("oppgave 1")

def legg_til_kontakt():
    kontaktliste = open("telefon.txt", "a")
    print("Legg til navn og nummer, avslutt med <enter>")
    ny_kontakt = input("Navn og nummer: ") + "\n"
    if ny_kontakt == "<enter>":
        kontaktliste.close()
    else:
        kontaktliste.write(ny_kontakt)
        kontaktliste.close()

legg_til_kontakt()

print("\n")


##Oppgave 2
print("oppgave 2")

def endre_nummer():
    ny_string = ""
    
    gammel_kontaktliste = open("telefon.txt", "r")
    str_gammel_kontaktliste = gammel_kontaktliste.read()
    
    ny_kontaktliste = open("nytelefon.txt", "a")
    navn = input("Navn:")
    navn_plassering = str_gammel_kontaktliste.find(navn)
    if navn_plassering == -1: return navn + "finnes ikke"
    
    start_nummer = navn_plassering + len(navn) + 1
    slutt_nummer = start_nummer + 8
    gammelt_nummer = str_gammel_kontaktliste[start_nummer:slutt_nummer]
    print(f"gammelt nummer: {gammelt_nummer}")
    nytt_nummer = input("Skriv nytt nummer:")
    
    ny_string = str_gammel_kontaktliste.replace(gammelt_nummer, nytt_nummer)
    ny_kontaktliste.write(ny_string)
    os.remove("telefon.txt")
    os.rename("nytelefon.txt", "telefon.txt")

    
endre_nummer()




##Oppgave 3
print("oppgave 3")


def fjerne_vokaler():
    orginale_vokaler = ["a", "e", "i", "o", "u", "y", "æ", "ø", "å"]
    ny_string = ""
    gammel_kineser = open ("treSmåKinesere.txt", "r")
    ny_kineser = open ("nytreSmåKinesere.txt", "a")
    #with open("treSmåKinesere.txt", "r") as gammel_kineser, open("ny_treSmåKinesere.txt", "a") as ny_kineser:
    linjer = gammel_kineser.readlines()
    ny_linjer = []
    for linje in linjer:
        for orginal_vokal in orginale_vokaler:
            linje = linje.replace(orginal_vokal, "")
        ny_linjer.append(linje)
    ny_string = ny_string.join(ny_linjer)

    ny_kineser.write(ny_string)        
    os.remove("treSmåKinesere.txt")
    os.rename("nytreSmåKinesere.txt", "treSmåKinesere.txt")    
        

fjerne_vokaler()





















