#Es1: ndarray, dtype, shape, arange
import numpy as np

seq1 = np.arange(10, 49) #come nei range, posso dare valore iniziale. Qua sto CREANDO un range.
print(seq1.dtype)
seq2 = np.array(seq1, dtype = "float64") #creo nuovo array con parametri seq1 (stessi valori), e nuovo tipo di dati
print(seq2.dtype)
print(seq1.shape)

#array crea un array vuoto con dei parametri, mentre arange crea la sequenza

