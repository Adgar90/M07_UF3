from connection import connection, conn

#Funció que ens permet actualitzar un movie dins de la taula
def updateMovie():
    #Query per actualitzar un movie
    sql = '''UPDATE public.movies
	SET movie_name='Pokemon', movie_genre='Anime', movie_director='Oda', movie_year=2001, movie_rate=9.9
	WHERE movie_id=1'''

    print(sql)

    #Usem mètode execute() per enviar la query
    connection.execute(sql)
    #Usem commit() per fer efectius els canvis de la query a la BD
    conn.commit()