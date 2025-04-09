#esercizio 2
class Libro :
    def __init__(self, titolo, autore, pagine): #metodo costruttore
        self.titolo = titolo #NON POSSO usare self per il titolo. Perchè self si riferisce a istanza
        self.autore = autore #attributi di istanza
        self.pagine = pagine
    
    def descrizione(self) :
        print("Il libro", self.titolo, "è stato scritto da", self.autore, "e ha", self.pagine, "pagine.")
#metodo che mi mostrerà output

cuore = Libro("cuore","De Amicis", "500")
divina_commedia = Libro("La Divina Commedia","Dante","1000")

cuore.descrizione()
divina_commedia.descrizione()



