#classe Biblioteca + permettere a utente di creare infiniti libri

class Biblioteca :
    def __init__(self, titolo) : #costruttore oggetti con titolo come attributo
        self.titolo = titolo
while True :
    scelta = input("Vuoi creare un libro?")
    if scelta == "si" : #se utente vuole aggiungere, faccio inserire
        self.titolo = input("Inserisci il nome del libro:") #con input definisco attributo titolo
        self = Biblioteca(self.titolo) #sto aggiungendo l'oggetto alla biblioteca 
        print("Hai aggiunto alla tua biblioteca:", self.titolo)
        continue
    else :
        break



        