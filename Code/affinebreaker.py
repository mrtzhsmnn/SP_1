#!/usr/bin/python
import ablib as ab
import aclib as ac
import sys

try: 
    datei=open(sys.argv[1],"r+") #Datei öffnen und in Variable speichern
    if(datei.read()==""): #Prüfung ob Datei leer ist
        print("Datei ist leer!") #Fehlermeldung ausgeben
        sys.exit() #Programm beenden
    datei.close() #Datei schließen
except IndexError: #Error handling
    print("Keine Datei angegeben!")  #Fehlermeldung, wenn zu wenige Parameter angegeben wurden.
    sys.exit() #Programm beenden
except FileNotFoundError: #Error handling 
    print("Datei existiert nicht!") #Fehlermeldung, wenn Datei nicht existiert
    sys.exit() #Programm beenden

datei=open(sys.argv[1],"r+") #Datei öffnen und in Variable speichern
cipher_text=datei.read() #Inhalt der Datei in Variable speichern


decoded_content=ac.decode(cipher_text) #Inhalt der Datei mit decode-Funktion konvertieren um anschließend computeFrequencyTable-Funktion mit Zahlen aufrufen zu können
freq_table=ab.computeFrequencyTable(decoded_content) #Frequenztabelle erstellen mit computeFrequencyTable-Funktion aus ablib 
print("Häufigkeitstabelle:")
ab.printFrequencyTable(freq_table) #Häufigkeitstabelle ausgeben

a=ab.computeMostFrequentChars(freq_table,4) #4 häufigsten Zeichen ermitteln mit computeMostFrequentChars-Funktion aus ablib
key_pairs=ab.computeKeyPairs(a) #Schlüsselpaare erstellen
print("Keypairs:" ,key_pairs) #Schlüsselpaare ausgeben

ab.analyzeCipherText(cipher_text,key_pairs) #Analyse des verschlüsselten Textes mit allen möglichen Schlüsseln
datei.close() #Datei schließen
