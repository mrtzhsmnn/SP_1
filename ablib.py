import aclib as ac # Importiere aclib
from collections import Counter # Counter() ist eine Klasse, die ein Dictionary erstellt

"""                 __PYTHON LIBRARY ABLIB__

    FUNKTIONEN:
        "computeFrequencyTable": 
            IN: Erwartet: Liste char_list 
            Berechnet Häufigkeitstabelle für die vorkommenden Zahlen in char_list.
            ==> Gibt Dictionary mit den Häufigkeiten der Zahlen zurück.
        "printFrequencyTable":
            IN: Ausgabe von computeFrequencyTable()
            Konvertiert die Zahlen der übergebenen Tabelle in Buchstaben und gibt sie wieder als Tabelle auf der Konsole aus.
            ==> Zahlen im von computeFrequencyTable() übergebenen Dictionary werden in Buchstaben konvertiert und als Tabelle ausgegeben
        "computeMostFrequentChars":
            IN: Erwartet: frequency_table, n 
            ==> Gibt Liste mit den n häufigsten Zahlen aus
        "computeKeyPairs":
            IN: Erwartet: char_list 
            berechnet alle möglichen Zahlenpaare (x,y) aus char_list
            ==> ohne ausgabe? oder mit?
        "analyzeCyphertext":
            IN: Erwartet: Geheimtext cypher_text, Liste von Zahlenpaaren char_pairs
            Geheimtext wird mit übergebenem Schlüssel entschlüsselt
            ==> Erste 50 Zeichen des entschlüsselten Textes werden ausgegeben
    VARIABELN:
        "":
            
""" 


#Hier kommen aufgabe 11, 12, 13, 14, 15 hinein

def computeFrequencyTable(char_list):
    # Erstelle leeres Dictionary
    freq_table = {}
    #Zählt die Häufigkeit, der in "char_list" vorkommenden Zahlen und füllt das Dicitonary mit den Werten
    for items in char_list:
        freq_table[items] = char_list.count(items) #count() gibt die Anzahl der Vorkommen der übergebenen Variable zurück
    return freq_table # Gibt Dictionary mit den Häufigkeiten der Zahlen zurück
def printFrequencyTable(freq_table):
    #TODO: key in Buchstaben umwandeln mit encode() statt manuell (Friedrich)
    for key, value in freq_table.items(): # Alle Items des Dictionaries durchlaufen
        # redundant, weil encode() diese Funktion bereits bietet, hat aber Fehler geworfen
        key = chr(key+97) #TODO: Fehlerfälle abfangen, optimieren, evtl. encode nutzen
        print(key, ' : ', value) # Ausgabe

def computeMostFrequentChars(freq_table, n):
    most_frequent = Counter(freq_table).most_common(n) # most_common() gibt die n häufigsten Werte zurück, allerdings nur als Tupel
    return [i[0] for i in most_frequent] # Tupel herausfiltern (i[0]) und nur die Zahlen zurückgeben


#Funktion "computeKeyPairs":
#   IN: Erwartet char_list als Liste von Zahlen in Z26.
#   Iteriert über char_list und berechnet die Paare (a,b) mit a!=b und a,b aus char_list.
#   ==> Gibt Liste von Paaren (a,b) char_pairs zurück.
def computeKeyPairs(char_list):
    #Rückgabeliste
    char_pairs = []
    #Doppelte Iteration über char_list (für a,b)
    for a in char_list:
        for b in char_list:
            #Prüfen, ob a!=b.
            if (a != b):
                char_pairs.append((a,b))
    return char_pairs


#def analyzeCipertext(cipher_text, char_pairs):
    # analyse
    # entschlüsseln mit gefundenenm Schlüsselpaar
    ac.acDecrypt(a, b, cypher_text)