giocatori = ["Lorenza","Mirko","Yasmine","Maria","Gaia"]
print("I giocatori sono Lorenza, Mirko, Yasmine, Maria e Gaia. Cosa vuoi fare? Puoi aggiungere, rimuovere o modificare i giocatori.")

scelta = input()

if scelta == "aggiungere" : 
    nuovo_giocatore = input("Dimmi il nome del nuovo giocatore:")
    giocatori.append(nuovo_giocatore)
    print("La tua nuova lista è", giocatori)
elif scelta == "modificare" :
    print(giocatori)
    tolto = input("chi vuoi sostituire?")
    sostituto = input("chi vuoi aggiungere?")
    giocatori.remove(tolto)
    giocatori.append(sostituto)
    print("La tua nuova lista è", giocatori)
elif scelta == "rimuovere" :
   eliminato = input("chi vuoi eliminare?")
   giocatori.remove(eliminato)
   print("La tua nuova lista è", giocatori)
else:
 print("comando sbagliato!")
   

    
