from connection import connection, conn

#Funció que ens permet esborrar una movie de la nostra taula
def deleteMovie():
    #Query per esborrar un nou movie
    sql = '''DELETE FROM public.movies
	WHERE movie_id=1;'''

    print(sql)

    #Usem mètode execute() per enviar la query
    connection.execute(sql)
    #Usem commit() per fer efectius els canvis de la query a la BD
    conn.commit()