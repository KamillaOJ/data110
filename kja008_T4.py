#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 12:07:41 2022

@author: kamilla
"""

# DATA110 Obligatorisk innleveringsoppgave Temainnlevering 4
# Egenretting 4


##Oppgave 1
print("oppgave 1")

def fak_for(n):   
    fak = 1
    for i in range(1, n + 1):
        fak = fak * i
    print(fak)
                
fak_for(4)

def fak_while(n):
    fak = 1
    new_fak = 1
    while fak < n + 1:
        new_fak = new_fak * fak
        fak = fak + 1
    print(new_fak)

fak_while(4)


#Oppgave 2
print("oppgave 2")

class Monark: 


    def __init__(self, nasjon, navn, tiltredelsesår, etterfølger = None):
        self.nasjon = nasjon
        self.navn = navn
        self.tiltredelsesår = tiltredelsesår
        self.etterfølger = etterfølger


    
    def settEtterfølger(self, neste):
        self.etterfølger = neste
        
    
    def skriv(self):
        if self.etterfølger != None:
            print(f"{self.navn} av {self.nasjon}, tiltrådt: {self.tiltredelsesår}, etterfølger: {self.etterfølger.navn}")
        else:
            print(f"{self.navn} av {self.nasjon}, tiltrådt: {self.tiltredelsesår}, etterfølger: {self.etterfølger}")
    
haakon = Monark('Norge','Kong Haakon VII', 1905)
olav = Monark("Norge", "Kong Olav V", 1957)   
harald = Monark("Norge", "Kong Harald V", 1991)

haakon.settEtterfølger(olav)
olav.settEtterfølger(harald)
harald.settEtterfølger(None)

kongerekke = [haakon]



kongerekke = [haakon, haakon.etterfølger, olav.etterfølger]


for monark in kongerekke:
     monark.skriv()





