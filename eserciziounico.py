#Punto 4: Utilizzo di if, while e for insieme

lista = []
while len(lista) <5 :
    numero = int(input("inserisci un numero:"))
    lista.append(numero)
    for numero in lista:
        numero_max = max(lista)
if len(lista) ==0 :
    print("La tua lista è vuota")
else : 
    print("Il numero più alto della tua lista è", numero_max, "e la tua lista ha", len(lista), "numeri.")


