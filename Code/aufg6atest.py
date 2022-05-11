import aclib as ac
teststring = 'strenggeheim'
print ('Testen von acEncrypt mit: ' + teststring )
a,b= ac.keyHelp ('db')
print ('Ergebnis: ' + ac.acEncrypt (a,b, teststring ))