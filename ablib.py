import aclib as ac

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
        # lesbarere Variante, jedoch langsamer
        freq_table[items] = char_list.count(items) #count() gibt die Anzahl der Vorkommen der übergebenen Variable zurück
        # oldschool Variante
        # if char in freq_table:
        #     freq_table[char] += 1
        # else:
        #     freq_table[char] = 1
    return freq_table # Gibt Dictionary mit den Häufigkeiten der Zahlen zurück
def printFrequencyTable(freq_table):
    #TODO: key in Buchstaben umwandeln mit encode() statt manuell (Friedrich)
    for key, value in freq_table.items():
        # redundant, weil encode() diese Funktion bereits bietet, hat aber Fehler geworfen
        key = chr(key+97)
        print(key, ' : ', value)

def computeMostFrequentChars(freq_table, n):
    most_frequent = []
    
    return most_frequent


#def computeKeyPairs(char_list):


#def analyzeCipertext(cipher_text, char_pairs):
