#!/usr/bin/python
import ablib as ab
import aclib as ac
import sys
import os


datei=open(sys.argv[1],"r")
cipher=datei.read()
decoded=ac.decode(cipher)
freq_table=ab.computeFrequencyTable(decoded)
print("Frequency Table:")
ab.printFrequencyTable(freq_table)
a=ab.computeMostFrequentChars(freq_table,4)
key_pairs=ab.computeKeyPairs(a)
print("Keypairs:" ,key_pairs)
ab.analyzeCipherText(cipher,key_pairs)
datei.close()