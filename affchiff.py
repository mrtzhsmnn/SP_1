#Programm zur Ver- und Entschlüsselung von affinen Chiffren


#Python Funktion "decode" erhält text und interpretiert die enthaltenen Buchstaben als Zahlen von 1-26.
#Ignoriert werden alle Sonderzeichen.
def decode(text):
    #Liste für Rückgabe erstellen
    retlist = []
    text.encode("ascii","ignore")
    #Alle Buchstaben in text klein
    text.casefold

    #While Schleife, durchläuft Code bis String leer. Interpretiere hier String als bool, wenn String leer, String = false.
    while text:
        #kopiere ersten Buchstaben in temp
        temp = text[:1]
        #fügt ans Ende der Liste retlist die Zahl an, ord gibt temp als asci, asci -96 ist Zahl im Alphabet.
        retlist.append(ord(temp) - 96)
        #ersten Buchstaben von text löschen
        text = text[1:]
    #gibt retlist zurück
    return retlist
    


#einfacher test
test = 'ABCD'
print(decode(test))


