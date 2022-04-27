#!/usr/bin/python
import ablib as ab
import sys
import os


with open(sys.argv[1], "r") as datei:
    lines = datei.read().split(',')

liste = []    
for line in lines:
    print(line)
    liste.append(line)
    
freq_table=ab.computeFrequencyTable(liste)
ab.printFrequencyTable(freq_table)
ab.computeMostFrequentChars(freq_table,n=6)
ab.computeKeyPairs(liste)
ab.analyzeCyphertext(datei,ab.computeKeyPairs(datei))

datei.close()




