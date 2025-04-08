# CREO LISTA per salvare numeri pari
numeri_pari = []

#Ciclo finchè non trovo 5 numeri pari
while len(numeri_pari) < 5 :
 numero = int(input("Inserisci un numero:"))
 if numero % 2 == 0 :
    print("Il numero è pari")
    numeri_pari.append(numero) #QUI AGGIUNGO elementi alla lista!!!
 else :
    print("Il numero è dispari")
print("Hai inserito 5 numeri pari:", numeri_pari)