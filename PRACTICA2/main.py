from connection import *
from create_table import * 
from create import *
from read import *
from update import *
from delete import *

#Funció que emula switch statement
def switch(option):
    if option=="1":
        insertMovie()
    elif option=="2":
        selectMovie()
    elif option=="3":
        updateMovie()
    elif option=="4":
        deleteMovie()
    else:
        return

try:
    #Preguntem a l'usuari si vol crear la taula
    response = input('Vols crear la taula? (yes/no): ')
    if (response == "yes"):
        createTable()
    #Iteració per execució de commandes SQL
    while True:
        command = input('INDICA LA COMANDA (0 per sortir) -> 1 INSERT 2 SELECT 3 UPDATE 4 DELETE : ')
        if (command == "0"): break
        switch(command)
except(Exception, psycopg2.Error) as error:
    print("Error", error)
finally:
    conn.close()

