while risposta == "si" :
   number = int(input("Inserisci un numero:"))
   for i in range (number, -1 , -1) : #qua lui capisce da solo che è fino a 0. Non serve un while i>0 xkè HO GIà DETTO CHE il range è fino a 0
      print(i)
risposta = int("vuoi ripetere?")
# Dò a risposta un valore iniziale, ma alla fine con la funzione input
# l'utente lo SOVRASCRIVE quindi può ricominciare o no il ciclo!