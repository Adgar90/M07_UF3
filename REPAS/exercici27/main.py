from suma_nums import suma
#Demanem dos números a l'usuari
x = int(input("Introdueix el primer número a sumar: "))
y = int(input("Introdueix el segon número a sumar: "))

#Mostrem el resultat de la funció cridada
print(f"{x} + {y} = {suma(x, y)}")