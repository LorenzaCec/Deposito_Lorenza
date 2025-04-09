class Punto : #nomino classe
    x = 10
    y = 20  #attributi della classe NO SBAGLIATO
    #devo per forza usare init per creare oggetti
    #quindi:
    # def __init__ (self, x, y):
    # self.x = x
    # self.y = y
    def muovi(self, dx, dy) :
        x = dx
        y = dy # attributi degli oggetti che modificano i valori iniziali
    def distanza_da_origine (self, distx, disty) : #la distanza è differenza da 0
        dx - 0 = distx #differenza da 0 non ha senso infatti!
        dy - 0 = disty
        print (self, "è distante", distx, disty, "da origine.")

punto1 = Punto(80,57)
punto2 = Punto(76,24)

punto1.distanza_da_origine()
punto2.distanza_da_origine()






