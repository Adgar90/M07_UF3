from connection import connection, conn

#Creació de taula a la BD
sql = '''CREATE TABLE MOVIES(
                movie_id SERIAL PRIMARY KEY,
                movie_name VARCHAR(255) NOT NULL,
                movie_genre VARCHAR(255) NOT NULL,
                movie_director VARCHAR(255) NOT NULL,
                movie_year BIGINT NOT NULL,
                movie_rate REAL NOT NULL
)'''

print(sql)

#Usem mètode execute() per enviar la query
connection.execute(sql)
#Usem commit() per fer efectius els canvis de la query a la BD
conn.commit()