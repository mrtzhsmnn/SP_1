#!/usr/bin/python
import ablib as ab
import aclib as ac
import sys

datei=open(sys.argv[1],"r") #Datei öffnen und in Variable speichern
cipher_text=datei.read() #Inhalt der Datei in Variable speichern
datei.close() #Datei schließen

decoded_content=ac.decode(cipher_text) #Inhalt der Datei mit decode-Funktion konvertieren um anschließend computeFrequencyTable-Funktion mit Zahlen aufrufen zu können
freq_table=ab.computeFrequencyTable(decoded_content) #Frequenztabelle erstellen mit computeFrequencyTable-Funktion aus ablib 
print("Frequency Table:")
ab.printFrequencyTable(freq_table) #Frequenztabelle ausgeben

a=ab.computeMostFrequentChars(freq_table,4) #4 häufigsten Zeichen ermitteln mit computeMostFrequentChars-Funktion aus ablib
key_pairs=ab.computeKeyPairs(a) #Schlüsselpaare erstellen
print("Keypairs:" ,key_pairs) #Schlüsselpaare ausgeben

ab.analyzeCipherText(cipher_text,key_pairs) #Analyse des verschlüsselten Textes mit allen möglichen Schlüsseln

