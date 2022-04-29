#!/usr/bin/python
import ablib as ab
import aclib as ac
import sys
import os

"""
with open(sys.argv[1], "r") as datei:
    lines = datei.read().split(',')

liste = []    
for line in lines:
    liste.append(line)
"""

datei=open(sys.argv[1],"r")
liste=datei.read()
liste=ac.decode(liste)
freq_table=ab.computeFrequencyTable(liste)
print(freq_table)
print("PrintFreqTable")
ab.printFrequencyTable(freq_table)
ab.computeMostFrequentChars(freq_table,n=3)
key_pairs=ab.computeKeyPairs(liste)
print("Keypairs:" ,key_pairs)
a=ab.analyzeCipherText(datei,ab.computeKeyPairs(datei))
print(a)
datei.close()




