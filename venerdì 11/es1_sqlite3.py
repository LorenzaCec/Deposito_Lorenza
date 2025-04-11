# creo database chiamato scuola.db

import sqlite3

conn = sqlite3.connect('scuola.db')

# creo tab chiamata studenti con diversi campi
cur = conn.cursor() #per creare cursore che mi esegue comandi SQL

cur.execute('''
    CREATE TABLE IF NOT EXISTS Studenti ( 
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT
    )
''') #aggiungo "If not exists" così SQL non dà errore qualora tabella Studenti esistesse già

# inserire 3 nomi di studenti
#prima creo funzione su python: xkè è variabile che creerò con python che mi darà variabile che uso con sqlite3
for i in range(3):  #funzione input dovrà essere ripetuta 3 volte: creo ciclo for e uso range per indicare 3 volte
    nome_inserito = input("Inserisci nome studente:")
    cur.execute("INSERT INTO Studenti (nome) VALUES (?)", (nome_inserito,))

conn.commit()

# leggi e stampa tutti i nomi di tabella studenti
print(cur.execute("SELECT * FROM Studenti")) #così non va bene: mi stampa il cursore!! Devo prima recuperare le righe
#versione corretta:
cur.execute("SELECT * FROM Studenti")
righe = cur.fetchall() #fetchall prende tutte le righe disponibili

for i in righe :
    print(i)

#fetchone
cur.execute("SELECT * FROM Studenti")
selez = cur.fetchone()
print(selez)