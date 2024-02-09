from connection import connection, conn

#Funció que ens permet insertar una movie a la nostra taula
def insertMovie():
    #Query per insertar un nou movie
    sql = '''INSERT INTO public.movies(
        movie_name, movie_genre, movie_director, movie_year, movie_rate)
        VALUES ('Terminator', 'Action', 'Bahawm', 1990, 9.5);'''

    print(sql)

    #Usem mètode execute() per enviar la query
    connection.execute(sql)
    #Usem commit() per fer efectius els canvis de la query a la BD
    conn.commit()