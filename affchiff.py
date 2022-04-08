#Programm zur Ver- und Entschlüsselung von affinen Chiffren


#Python Funktion "decode" erhält text und interpretiert die enthaltenen Buchstaben als Zahlen von 1-26.
#Ignoriert werden alle Sonderzeichen.
def decode(text):
    #Liste für Rückgabe erstellen, String für gefilterten Text erstellen
    retlist = []
    textfilt = ''
    #Alle nicht Ascii-Zeichen löschen
    text.encode("ascii","ignore")
    #Alle Buchstaben in text klein
    text = text.casefold()
    #Nur kleine alphabetische zeichen im String belassen:
    #x ist i-ter Buchstabe aus text
    for x in text:
        #x wird in ascii interpretiert, alles was nicht kleinbuchstabe ist wird verworfen (kleinbuchstabe in ascii zw. 97-122)
        if (ord(x) >= 97 and ord(x) <= 122):
            #wenn kleinbuchstabe, an textfilt anhängen
            textfilt += x
            
    #While Schleife, durchläuft Code bis String leer. Interpretiere hier String als bool, wenn String leer, String = false.
    while textfilt:
        #kopiere ersten Buchstaben in temp
        temp = textfilt[:1]
        #fügt ans Ende der Liste retlist die Zahl an, ord gibt temp als asci, asci -96 ist Zahl im Alphabet.
        retlist.append(ord(temp) - 97)
        #ersten Buchstaben von text löschen
        textfilt = textfilt[1:]
    #gibt retlist zurück
    return retlist
    


#einfacher test
test = 'Hallo Welt!'
print(decode(test))



testschwer = '# `P Ü h ||.R{ h'
print(decode(testschwer))
