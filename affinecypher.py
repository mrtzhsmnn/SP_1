#!/usr/bin/python
import aclib as ac
import sys
import os


try: 
    mode=sys.argv[1] #Variablen zuweisen (Ver-/Entschlüsseln)
    key=sys.argv[2]  #Variablen zuweisen (Schlüssel)
    path=sys.argv[3] #Variablen zuweisen (Dateipfad)
except: #Error handling
    print("Zu wenige Parameter angegeben!")  #Fehlermeldung, wenn zu wenige Parameter angegeben wurden.
    sys.exit() #Programm beenden 

a,b=ac.keyHelp(key) #Key wird in Keyhelp-Funktion zerlegt und in a und b gespeichert

if(mode!='e' and mode!='d'): #Prüfung ob mode gültig ist   
    print("Kein gültiger Modus!") #Fehlermeldung ausgeben
    sys.exit() #Programm beenden
try: #Prüfung ob Datei existiert
    datei=open(path, "r+") #Datei öffnen und in Variable speichern

except: #Wenn Datei nicht existiert
    print("Datei nicht gefunden!") #Fehlermeldung ausgeben
    sys.exit() #Programm beenden

if(mode == 'e'): #Wenn mode "e" ist (verschlüsseln)
    newContent=ac.acEncrypt(a,b,datei.read()) #Neuer Inhalt der Datei mit acEncrypt
    datei.close() #Datei schließen
    if(newContent==""):
        sys.exit() #Programm beenden    
    else:
        os.remove(path) #Datei löschen
        datei=open(path, "w+")
        datei.write(newContent) #verschlüsselter Inhalt wird in Datei geschrieben
        print("Datei wurde verschlüsselt!") #Meldung ausgeben
elif(mode == 'd'): #Wenn mode "d" ist (entschlüsseln)
    newContent=ac.acDecrypt(a,b,datei.read()) #Neuer Inhalt der Datei mit acDecrypt
    datei.close() #Datei schließen
    if(newContent==""):
        sys.exit() #Programm beenden
    else:
        os.remove(path) #Datei löschen  
        datei=open(path, "w+")
        datei.write(newContent) #entschlüsselter Inhalt wird in Datei geschrieben
        print("Datei wurde entschlüsselt!") #Meldung ausgeben
datei.close() #Datei schließen


#Die Datei ist nun entweder verschlüsselt oder entschlüsselt und kann im nächsten Schritt ausgegeben werden 
with open(path, "r") as datei: #Datei öffnen
    print(datei.read()) #Inhalt der Datei ausgeben