nomi = ["lodry", "yas", "gaia", "Pini"]
numeri = [3,5,76,8,90]
misto = ["mamma", 8, 54, "nikky"]

print(nomi[2])
print(misto[0])
misto[2]="papà"
print(misto[2])

inserimento = input("inserisci un nome:")
nomi.append(inserimento)
print(nomi)
nomi.insert(2,"Mimi")
print(nomi)