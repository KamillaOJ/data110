#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 16:45:25 2022

@author: kamilla
"""

#DATA110 Obligatorisk innleveringsoppgave 3
#Temainnlevering 3

##Oppgave 1
print("oppgave 1a")
x = 9
y = 66
print(x != 7) ## True når x = 9
print(y <= 50) ## False når y = 66
print(x != 7 and y <= 50) ## False når x = 9 og y = 66
print((x > 7 or 50 < y) and (x > y or y < 100)) ## True når x = 9 og y = 66


print("oppgave 1b")
print(x != 7 and y <= 50)
# er ekvivaltent med: 
print(y <= 50 and x != 7)
# og:
print((x < 7 or x > 7) and (y < 50 or y == 50))
# (jeg skjønner ikke oppgaven, skal vi finne en lengre, men lik måte å skrive 
# uttrykket på?)



##Oppgave 2
print("oppgave 2")
print("Vil du bli ordfører eller sitte i bystyret i Tulleby?")
alder = int(input("Oppgi alder:"))
bodd_år = int(input("Hvor lenge har du bodd i Tulleby? \nOppgi lengde i antall år:"))
if alder >= 30 and bodd_år >= 9:
    print("Du kan bli ordfører eller sitte i bystyret")
elif alder >= 25 and bodd_år >= 5:
    print("Du kan sitte i bystyret")
    ordår_alder = 30 - alder
    ordår_bodd = 9 - bodd_år
    if ordår_alder > ordår_bodd:
        print(f"Prøv igjen om {ordår_alder} år for å blir ordfører")
    if ordår_alder < ordår_bodd:
        print(f"Prøv igjen om {ordår_bodd} år for å bli ordfører")
else:
    print("Du kan verken bli ordfører eller sitte i bystyret")
    ordår_alder = 30 - alder
    ordår_bodd = 9 - bodd_år
    styrår_alder = 25 - alder
    styrår_bodd = 5 - bodd_år
    if styrår_alder > styrår_bodd:
        print(f"Prøv igjen om {styrår_alder} år for å sitte i bystyret")
    if styrår_alder < styrår_bodd:
        print(f"Prøv igjen om {styrår_bodd} år for å sitte i bystyret")
    if ordår_alder > ordår_bodd:
        print(f"Prøv igjen om {ordår_alder} år for å blir ordfører")
    if ordår_alder < ordår_bodd:
        print(f"Prøv igjen om {ordår_bodd} år for å bli ordfører")



##Oppgave 3
print("oppgave 3")

## Orginal:
# x=int(input('tall:'))
# if x>5 :
#       if x<10 :
#         print('6,7,8 eller 9')
#       if x>=10:
#         print('minst 10')
# if x<=5 :
#     print('max 5')

## uten nesting:
x = int(input('tall:'))
if x > 5 and x < 10:
    print('6,7,8 eller 9')
elif x > 5 and x >= 10:
    print('minst 10')
elif x <= 5:
    print('max 5')




































