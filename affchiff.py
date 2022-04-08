#Programm zur Ver- und Entschlüsselung von affinen Chiffren


#Python Funktion "decode": 
#   Erhält text und interpretiert die enthaltenen Buchstaben als Zahlen von 0-25.
#   Ignoriert werden alle Leer- und Sonderzeichen.
#   Alle Großgeschriebenen Buchstaben werden als kleine interpretiert
#   ==> Gibt Liste mit Zahlenwerten zurück.
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


#Python Funktion "encode":
#   Erhält Liste char_list und interpretiert die enthaltenen Zahlen von 0-25, als Kleinbuchstaben
#   ==> Gibt String mit text zurück.
def encode(char_list):
    #def. String für Rückgabe
    retstring = ''
    #for-schleife x nimmt i-ten Wert aus char_list an
    for x in char_list:
        #retstring wird um den Charakter von (x + 97) als ASCII-Wert interpretiert erweitert.
        retstring += chr(x+97)
    #gebe retstring zurück
    return retstring    


#--TESTS:--
#Test von decode wie in Aufgabenstellung:
print('Test von "decode" mit: ')
test = 'Hallo Welt!'
print(test)
print(decode(test))
print('-----------------------------------------')
#Test von decode mit schwerem String:
print('Test von "decode" mit: ')
testschwer = '# `P Ü h ||.R{ h'
print(testschwer)
print(decode(testschwer))
print('-----------------------------------------')
#Test von encode mit Aufgabenstellung:
char_list = [13, 0, 2, 7, 17, 8, 2, 7, 19]
print('Test von "encode" mit: ')
print(char_list)
print('Ergebnis: ' + encode(char_list))
