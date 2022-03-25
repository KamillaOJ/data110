#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 15:34:15 2022

@author: kamilla
"""

#DATA110 Obligatorisk innleveringsoppgave 1
#Temainnlevering 1



##Oppgave 1
print("oppgave 1a")
print("Kamilla")
print("Ormevik")
print("Jansen")
print("\n")


print("oppgave 1b")
print("Kamilla", "Ormevik", "Jansen", sep = "\n")
print("\n")



##Oppgave 2
#Har bare skrevet de 3 første bokstavene siden jeg har langt navn

print("oppgave 2")
print("*    *      **         *      *")
print("*   *      *  *       * *    * *")
print("*  *      *    *     *   * *    *")
print("* *      *      *   *     *      *")
print("**      *        * *              *")
print("* *     ********** *              *")
print("*  *    *        * *              *")
print("*   *   *        * *              *")
print("*    *  *        * *              *")
print("*     * *        * *              *")
print("\n")



##oppgave 3
print("oppgave 3")

nok = input("skriv verdi i norske kroner:")
nok = int(nok)
euro = 0.10248
dollar = 0.1162
print("\n")

print("oppgave 3a")
print(f"{nok} kroner tilsvarer {nok*euro} Euro og {nok*dollar} Dollar")
print("\n")


print("oppgave 3b")

eurosign = (u"\N{euro sign}")
dollarsign = (u"\N{dollar sign}")
print(f"{nok} kroner tilsvarer {nok*euro} {eurosign} og {nok*dollar} {dollarsign}")






