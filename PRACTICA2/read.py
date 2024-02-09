from connection import connection, conn

#Funció que ens permet consultar les dades de la nostra taula
def selectMovie():
    #Query per consultar les dades dels movies de la BD
    sql = '''SELECT movie_id, movie_name, movie_genre, movie_director, movie_year, movie_rate
	FROM public.movies;'''

    print(sql)

    #Usem mètode execute() per enviar la query
    connection.execute(sql)

    #Usem commit() per fer efectius els canvis de la query a la BD
    conn.commit()

    #Agafem els resultats de la consulta i els mostrem
    resultats = connection.fetchall()
    for movie in resultats:
        print(movie)