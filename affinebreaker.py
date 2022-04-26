#!/usr/bin/python
import ablib as ab
import sys
import os

print("cock")
datei=open(sys.argv[1],"r")
<<<<<<< HEAD
print (ab.computeFrequencyTable(datei))
=======

ab.computeFrequencyTable(datei)
>>>>>>> d4635e60be79dbdb1758e2134868822b118eeb50
ab.printFrequencyTable(datei)
ab.computeMostFrequentChars(datei,3)
ab.computeKeyPairs(datei)
ab.analyzeCyphertext(datei,ab.computeKeyPairs(datei))
<<<<<<< HEAD
datei.close()
=======
>>>>>>> d4635e60be79dbdb1758e2134868822b118eeb50

