import sqlalchemy as db
import sqlalchemy.dialects.postgresql.psycopg2


class Database():
    #Connessione al db usando un engine, modo 1
    engine = db.create_engine('postgresql://postgres:a@localhost/UCI Cinema')
    def __init__(self):
        self.connection = self.engine.connect()
        print("DB Instance created")
        
def fetchByQyery(self, query):
    fetchQuery = self.connection.execute(f"SELECT * FROM {query}")
        
    for data in fetchQuery.fetchall():
        print(data)

"""import psycopg2

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
"""