"""                 __PYTHON LIBRARY ACLIB__

    FUNKTIONEN:
        "decode": 
            IN: Erwartet String text.
            Interpretiert die in text enthaltenen Buchstaben als Zahlen von 0-25.
            Ignoriert werden alle Leer- und Sonderzeichen.
            Alle Großgeschriebenen Buchstaben werden als kleine interpretiert
            ==> Gibt Liste mit Zahlenwerten zurück.
        "encode":
            IN: Erwartet Liste char_list.
            Interpretiert die in char_list enthaltenen Zahlen von 0-25, als Kleinbuchstaben.
            (Umkehrfunktion zu decode)
            ==> Gibt String mit text zurück.
        "acEncrypt":
            IN: Erwartet Schlüssel a, und b, beide müssen in key_table sein.
                Erwartet String plain_text mit dem zu verschlüsselnden Text.
            Verschlüsselt plain_text mit dem Schlüsselpaar a & b.
            Fehler, falls mind. einer der Schlüssel ungültig. => Fehlermeldung wird ausgegeben, leerer String zurückgegeben.
            ==> Gibt String mit verschlüsseltem Text zurück (nur Großbuchstaben), bei Fehler leeren String.
        "acDecrypt":
            IN: Erwartet Schlüssel a, und b, beide müssen in key_table sein.
                Erwartet String cypher_text mit dem zu entschlüsselnden Text.
            Entschlüsselt cypher_text mit dem Schlüsselpaar a & b.
            Fehler, falls mind. einer der Schlüssel ungültig. => Fehlermeldung wird ausgegeben, leerer String zurückgegeben.
            ==> Gibt String mit entschlüsseltem Text zurück (nur Kleinbuchstaben), bei Fehler leeren String.
        "keyHelp" (Hilfsfunktion):
            IN: Erwartet String mit Schlüsselpaar z.b. 'db'.
            Prüft und decoded Schlüsselpaar, PRÜFT NICHT AUF KORREKTHEIT DES SCHLÜSSELPAARS!
            ==> Gibt zwei Zahlen a,b als Int zurück, beide Zahlen 27 wenn Fehler.
    VARIABELN:
        "key_table":
            Dictionary mit a und der passenden inversen a^-1 in Z26
            Es werden nur a als Schlüssel akzeptiert für die a^-1 in Z26 liegt.
            Daher hier nur ausgewählte Paare.
            ==>Paart a mit den inversen Elementen.
""" 



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
        #fügt ans Ende der Liste retlist die Zahl an, ord gibt temp als ascii, ascii-wert abzuüglich 96 ist Zahl im Alphabet.
        #Hier -97, da Zahlen nicht von 1-26 sondern von 0-25 angegeben werden sollen.
        retlist.append(ord(temp) - 97)
        #ersten Buchstaben von text löschen
        textfilt = textfilt[1:]
    #gibt retlist zurück
    return retlist

def encode(char_list):
    #def. String für Rückgabe
    retstring = ''
    #for-schleife x nimmt i-ten Wert aus char_list an
    for x in char_list:
        #retstring wird um den Charakter von (x + 97) als ASCII-Wert interpretiert erweitert.
        retstring += chr(x+97)
    #gebe retstring zurück
    return retstring    

key_table = {
    1 : 1,
    3 : 9,
    5 : 21,
    7 : 15,
    9 : 3,
    11 : 19,
    15 : 7,
    17 : 23,
    19 : 11,
    21 : 5,
    23 : 17,
    25 : 25
}

def acEncrypt(a, b , plain_text):
    #String für return
    retstring = ''
    #Liste um Zahlen zur Manipulation zu speichern. i für counter bei for-Schleife
    worklist = []
    i = 0
    #Prüfen, ob beide Keys in key_table liegen (nur dann hat man gültiges Schlüsselpaar).
    if not((a in key_table) and (b in key_table)):
        #Wenn einer der beiden Keys ungültig, Fehlermeldung ausgeben und leeren String zurückgeben.
        print('FEHLER: mindestens einer der Keys im KEYPAIR ist ungültig!')
        return retstring
    #plain_text in liste von Zahlen umwandeln mit decode.
    worklist = decode(plain_text)
    #Worklist durchlaufen, wert immer in x speichern.
    for x in worklist:
        #Worklist an i-ter Stelle mit verschl. Text füllen.
        worklist[i] = ((a*x + b) %26)
        #i um 1 erhöhen.
        i+=1 
    #Worklist in text umwandeln mit encode.
    retstring = encode(worklist)
    #Return Retstring in großbuchstaben
    return retstring.swapcase()

def acDecrypt(a, b, cypher_text):
    #Liste um Zahlen zur Manipulation zu speichern. i für counter bei for-Schleife
    worklist = []
    i = 0
    #Prüfen, ob beide Keys in key_table liegen (nur dann hat man gültiges Schlüsselpaar).
    if not((a in key_table) and (b in key_table)):
        #Wenn einer der beiden Keys ungültig, Fehlermeldung ausgeben und leeren String zurückgeben.
        print('FEHLER: mindestens einer der Keys im KEYPAIR ist ungültig!')
        return ''
    #cypher_text in Liste von Zahlen umwandeln mit decode.
    worklist = decode(cypher_text)
    #Worklist durchlaufen, wert immer in x speichern.
    for x in worklist:
        #Worklist an i-ter Stelle mit entschl. Text füllen. Formel siehe Aufgabenstellung Inverses zu a ist in key_table
        worklist[i] = (((x-b) * key_table[a])%26)
        #i um 1 erhöhen.
        i+=1 
    #Worklist mit Encode zu string umwandeln und zurückgeben.
    return encode(worklist)

def keyHelp(key):
    #Sicherstellen, dass String tatsächlich nur 2 char enthält.
    if len(key) == 2 :
        #String decoden und in Worklist speichern.
        worklist = decode(key)
        #prüfen, ob worklist auch noch 2 Elemente hat, oder ob decode Zeichen aussortiert hat
        if len(worklist) == 2 :
            #einzelne Keys aus Worklist zurückgeben
            return worklist[0],worklist[1]
        else:
            print('Im vorliegenden String waren verbotene Zeichen, Sodass er beim Aufruf von "decode" verkürzt wurde!')
            return 27,27
    else: 
        print('Der String ist entweder <2 oder >2 Zeichen. Ein keypair besteht aus 2 Zeichen.')
        return 27,27