import aclib as ac
from collections import Counter
from math import gcd

# Funktion "computeFrequencyTable": 
# IN: Erwartet: Liste char_list 
# Berechnet Häufigkeitstabelle für die vorkommenden Zahlen in char_list.
# ==> Gibt Dictionary mit den Häufigkeiten der Zahlen zurück.
def computeFrequencyTable(char_list):
    # Erstelle leeres Dictionary
    freq_table = {}
    #Zählt die Häufigkeit, der in "char_list" vorkommenden Zahlen und füllt das Dicitonary mit den Werten
    for items in char_list:
        freq_table[items] = char_list.count(items) #count() gibt die Anzahl der Vorkommen der übergebenen Variable zurück
    return freq_table # Gibt Dictionary mit den Häufigkeiten der Zahlen zurück

# Funktion "printFrequencyTable":
# IN: Ausgabe von computeFrequencyTable()
# Konvertiert die Zahlen der übergebenen Tabelle in Buchstaben und gibt sie wieder als Tabelle auf der Konsole aus.
# ==> Zahlen im von computeFrequencyTable() übergebenen Dictionary werden in Buchstaben konvertiert und als Tabelle ausgegeben
def printFrequencyTable(freq_table):
    for key, value in freq_table.items(): # Alle Items des Dictionaries durchlaufen
        key = chr(key+97) # Jeweils gefunden key in Unicode-Zeichen umwandeln
        print(key, ' : ', value) # formatierte Ausgabe

# Funktion "computeMostFrequentChars":
# IN: Erwartet: frequency_table, n 
# ==> Gibt Liste mit den n häufigsten Zahlen aus
def computeMostFrequentChars(freq_table, n):
    most_frequent = Counter(freq_table).most_common(n) # most_common() gibt die n häufigsten Werte zurück, allerdings nur als Tupel
    return [i[0] for i in most_frequent] # Tupel herausfiltern (i[0]) und nur die Zahlen zurückgeben

# Funktion "computeKeyPairs":
# IN: Erwartet char_list als Liste von Zahlen in Z26.
# Iteriert über char_list und berechnet die Paare (a,b) mit a!=b und a,b aus char_list.
# ==> Gibt Liste von Paaren (a,b) char_pairs zurück.
def computeKeyPairs(char_list):
    # Rückgabeliste
    char_pairs = []
    # Doppelte Iteration über char_list (für a,b)
    for a in char_list:
        for b in char_list:
            #Prüfen, ob a!=b.
            if (a != b):
                char_pairs.append((a,b))
    return char_pairs

# Funktion "analyzeCyphertext":
# IN: Erwartet: Geheimtext cypher_text, Liste von Zahlenpaaren char_pairs
# Geheimtext wird mit übergebenem Schlüssel entschlüsselt
# ==> Erste 50 Zeichen des entschlüsselten Textes werden ausgegeben
def analyzeCipherText(cipher_text, char_pairs):
    # iteriere über char_pairs
    for cE, cN in char_pairs:
        # berechne mögliches Schlüsselpaar für jedes cE, cN
        a = (3 * (cN - cE)) % 26
        b = (cE - (4 * a)) % 26
        # Prüfen ob gefundener Schlüssel plausibel ist
        if gcd(a,26) != 1 or b > 26:
            # nächste Iteration, falls unplausibel
            continue
        else:
            print("Möglicher Schlüssel:" , "a:", a, "b:", b)
            print('Mögliches Ergebnis: ')
            # entschlüssle cipher_text mit gefundenem Schlüsselpaar
            plain_text = ac.acDecrypt(a, b, cipher_text)
            # gib die ersten 50 Zeichen von plain_text aus
            return print(plain_text[:50])
    
