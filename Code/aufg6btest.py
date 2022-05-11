import aclib as ac
teststring = 'IFFYVQMJYFFDQ'
print('Testen von acDecrypt mit : ' + teststring)
a,b=ac.keyHelp('pi')
print('Ergebnis: ' + ac.acDecrypt(a,b,teststring))