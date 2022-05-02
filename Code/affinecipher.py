#!/usr/bin/python
import aclib as ac
import sys
import os


try: 
    mode=sys.argv[1] #Variablen zuweisen (Ver-/Entschlüsseln)
    key=sys.argv[2]  #Variablen zuweisen (Schlüssel)
    path=sys.argv[3] #Variablen zuweisen (Dateipfad)
    datei=open(path,"r+") #Datei öffnen und in Variable speichern
    oldContent=datei.read() #Inhalt der Datei in Variable speichern
    if(mode!='e' and mode!='d'): #Prüfung ob mode gültig ist   
        print("Kein gültiger Modus!") #Fehlermeldung ausgeben
        sys.exit() #Programm beenden
    if(oldContent==""):
        print("Datei ist leer!") #Wenn Datei leer ist Hinweis ausgeben und anschließend Programm beenden
        sys.exit()
except IndexError: #Error handling: Wenn zu wenige Parameter angegeben wurden
    print("Zu wenige Parameter angegeben!")  #Fehlermeldung, wenn zu wenige Parameter angegeben wurden.
    sys.exit() #Programm beenden 
except FileNotFoundError: #Error handling: Wenn Datei nicht existiert
    print("Datei existiert nicht!") #Fehlermeldung, wenn Datei nicht existiert
    sys.exit() #Programm beenden

a,b=ac.keyHelp(key) #Key wird in Keyhelp-Funktion zerlegt und in a und b gespeichert

#Entscheiden welcher Modus gewählt wurde: 
if(mode == 'e'): #Wenn mode "e" ist (verschlüsseln)
    newContent=ac.acEncrypt(a,b,oldContent) #Neuer Inhalt der Datei mit acEncrypt verschlüsselt, hierbei wird auch das Schlüsselpaar überprüft
    datei.close() #Datei schließen um sie anschließend löschen zu können
    os.remove(path) #Datei löschen um sie neu zu erstellen, um whitespaces zu verhindern
    datei=open(path, "w+") #Datei wird neu erstellt und geöffnet, um diese befüllen zu können
    datei.write(newContent) #verschlüsselter Inhalt wird in Datei geschrieben
    print("Datei wurde verschlüsselt!") #Meldung ausgeben
elif(mode == 'd'): #Wenn mode "d" ist (entschlüsseln)
    newContent=ac.acDecrypt(a,b,oldContent) #Neuer Inhalt der Datei mit acDecrypt entschüsselt, und Schlüsselpaare überprüft
    datei.close() #Datei schließen um sie anschließend löschen zu können
    os.remove(path) #Datei löschen um beim befüllen whitespaces zu verhindern   
    datei=open(path, "w+") #Datei wird neu erstellt und geöffnet, um diese befüllen zu können
    datei.write(newContent) #entschlüsselter Inhalt wird in Datei geschrieben
    print("Datei wurde entschlüsselt!") #Meldung ausgeben
datei.close() #Datei schließen

#Die Datei ist nun entweder verschlüsselt oder entschlüsselt und kann im nächsten Schritt ausgegeben werden 
with open(path, "r") as datei: #Datei öffnen
    print(datei.read()) #Inhalt der Datei ausgeben
