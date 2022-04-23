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
    freq_table = {}
    for char in char_list:
        if char in freq_table:
            freq_table[char] += 1
        else:
            freq_table[char] = 1
    return freq_table
    #Zählt die Häufigkeit, der in "char_list" vorkommenden Zahlen
    #char_list.value_counts()

def printFrequencyTable(freq_table):
    #Liste für Rückgabe erstellen
    for key, value in freq_table.items():
        print ("% d : % d"%(key, value))

def computeMostFrequentChars(freq_table, n):
    #Liste für Rückgabe erstellen


def computeKeyPairs(char_list):
    #Liste für Rückgabe erstellen


def analyzeCipertext(cipher_text, char_pairs):
    #Liste für Rückgabe erstellen
