#Crear un diccionari { key(nom) : value(edat) }
#Variable en empty
myDict = {}

#Print informatiu per saber el funcionament del programa
print("Introdueix el nom i l'edat per afegir o escriu SORTIR per sortir.")
print()
#Bucle que demana dades per introduir al nostre diccionari o sortir en cas de no voler continuar
while True:
    name = input("Introdueix un nom: ")
    #Condicional que atura el bucle en cas que l'usuari vulgui sortir
    if (name.upper() == "SORTIR"): break
    age = int(input("Introdueix una edat: "))
    myDict.update({name:age})

#Mostrem el nostre diccionari
print(myDict)