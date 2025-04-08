# Punto 3: Utilizzo di for

lista = [] #creo lista vuota
numero1 = int(input("Scrivi un numero:"))
lista.append(numero1)
numero2 = int(input("Scrivi un altro numero:"))
lista.append(numero2)
numero3 = int(input("Scrivi un altro numero:"))
lista.append(numero3)
#creo lista per i quadrati
quadrati = []
for numero in lista : 
    quadrati.append(numero**2)
print("Ecco i quadrati della lista:", quadrati)
