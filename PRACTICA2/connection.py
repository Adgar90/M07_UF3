import psycopg2

#Connexió a la base de dades
conn = psycopg2.connect(
    database="postgres",
    user="admin",
    password="admin",
    host="localhost",
    port="5432"
)

#Fem cursor() per realitzar la connexió amb la BD
connection = conn.cursor()

print(connection)