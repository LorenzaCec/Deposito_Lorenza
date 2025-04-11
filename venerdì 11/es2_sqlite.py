# creo database chiamato Libreria.db
import sqlite3

conn = sqlite3.connect('Libreria.db')
cur = conn.cursor()
 
#creo tabella 

cur.execute('''
    CREATE TABLE IF NOT EXISTS Libri (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titolo TEXT,
        autore TEXT
    )
''')

#inserire 3 libri con metodo execute many : serve lista!
lista_libri= []

for i in range(3):
    nome_libro = input("Inserisci libro in Libreria:")
    autore_libro = input("Inserisci autore:")
    lista_libri.append((nome_libro, autore_libro))


cur.executemany('INSERT INTO Libri (titolo, autore) VALUES (? , ?)', lista_libri)

conn.commit()

#recupero e stampo

cur.execute('SELECT * FROM Libri')
righe = cur.fetchall()
for i in righe :
    print(i)

