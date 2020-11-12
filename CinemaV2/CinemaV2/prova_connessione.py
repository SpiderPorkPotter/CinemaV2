import psycopg2

con = psycopg2.connect(database="UCI Cinema", user="postgres", password="a", host="localhost", port="5432")
print("Database opened successfully")

cur = con.cursor()
cur.execute("SELECT nome, cognome, telefono, email, password from Utenti")
rows = cur.fetchall()

for row in rows:
    print("ADMISSION =", row[0])
    print("NAME =", row[1])
    print("AGE =", row[2])
    print("COURSE =", row[3])
    print("DEPARTMENT =", row[4], "\n")

print("Operation done successfully")
con.close()

#non riesco a capire cosa sbaglio nella query
#ho preso l'esempio da questo sito: https://stackabuse.com/working-with-postgresql-in-python/