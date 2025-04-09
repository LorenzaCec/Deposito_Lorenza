# 1) creo array 
import numpy as np

seq1 = np.random.randint(10, 50, size = 20) #inizio, fine e quantità dei numeri generati random

# 2) Estrarre primi 10 elementi di array
punto_2 = seq1[:9] #non mettere 0, semplicemente lo ometto!!

# 3) estrarre ultimi 5
punto_3 = seq1[14:] #stessa cosa ometto lo stop!!!

# 4) estrarre da 5 a 15
punto_4 = seq1[4:14]

# 5) estrarre ogni terzo elemento di array
punto_5 = seq1[:19:3]

# 6) modificare elementi da 5 a 10, assegnando valore di 99
seq2 = np.array(seq1)
seq2[4:10] = 99

# 7) stampo tutto
print(seq1)
print(punto_2)
print(punto_3)
print(punto_4)
print(punto_5)
print(seq2)