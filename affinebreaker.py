#!/usr/bin/python
import ablib as ab
import sys
import os

print("cock")
datei=open(sys.argv[1],"r")
print (ab.computeFrequencyTable(datei))
ab.printFrequencyTable(datei)
ab.computeMostFrequentChars(datei,3)
ab.computeKeyPairs(datei)
ab.analyzeCyphertext(datei,ab.computeKeyPairs(datei))
datei.close()

