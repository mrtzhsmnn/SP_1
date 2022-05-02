#!/usr/bin/python
import aclib as ac
import sys
import os


try: 
    mode=sys.argv[1] #Variablen zuweisen (Ver-/Entschlüsseln)
    key=sys.argv[2]  #Variablen zuweisen (Schlüssel)
    path=sys.argv[3] #Variablen zuweisen (Dateipfad)
    datei=open(path,"r+") #Datei öffnen und in Variable speichern
    if(mode!='e' and mode!='d'): #Prüfung ob mode gültig ist   
        print("Kein gültiger Modus!") #Fehlermeldung ausgeben
        sys.exit() #Programm beenden
    if(datei.read()==""):
        print("Datei ist leer!")
        sys.exit()
except IndexError: #Error handling
    print("Zu wenige Parameter angegeben!")  #Fehlermeldung, wenn zu wenige Parameter angegeben wurden.
    sys.exit() #Programm beenden 
except FileNotFoundError: #Error handling
    print("Datei existiert nicht!") #Fehlermeldung, wenn Datei nicht existiert
    sys.exit() #Programm beenden
datei.close() #Datei schließen
a,b=ac.keyHelp(key) #Key wird in Keyhelp-Funktion zerlegt und in a und b gespeichert
datei=open(path,"r+") #Datei öffnen und in Variable speichern
#Entscheiden welcher Modus gewählt wurde: 
if(mode == 'e'): #Wenn mode "e" ist (verschlüsseln)
    newContent=ac.acEncrypt(a,b,datei.read()) #Neuer Inhalt der Datei mit acEncrypt
    datei.close() #Datei schließen
    os.remove(path) #Datei löschen
    datei=open(path, "w+") #Datei wird neu erstellt und geöffnet, um diese befüllen zu können
    datei.write(newContent) #verschlüsselter Inhalt wird in Datei geschrieben
    print("Datei wurde verschlüsselt!") #Meldung ausgeben
elif(mode == 'd'): #Wenn mode "d" ist (entschlüsseln)
    newContent=ac.acDecrypt(a,b,datei.read()) #Neuer Inhalt der Datei mit acDecrypt
    datei.close() #Datei schließen
    os.remove(path) #Datei löschen  
    datei=open(path, "w+") #Datei wird neu erstellt und geöffnet, um diese befüllen zu können
    datei.write(newContent) #entschlüsselter Inhalt wird in Datei geschrieben
    print("Datei wurde entschlüsselt!") #Meldung ausgeben
datei.close() #Datei schließen

#Die Datei ist nun entweder verschlüsselt oder entschlüsselt und kann im nächsten Schritt ausgegeben werden 
with open(path, "r") as datei: #Datei öffnen
    print(datei.read()) #Inhalt der Datei ausgeben
