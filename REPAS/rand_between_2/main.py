from rand_between_2 import aleatori
#Demanem els valors (supossem que posan integers)
x = int(input("Introdueix el primer número: "))
y = int(input("Introdueix el segon número: "))

#Cridem la funció amb una ternaria per evitar errors a l'hora de passar els paràmetres
numero_aleatori = aleatori(x, y) if x<y else aleatori(y, x)
#Mostrem el resultat
print(f"El número aleatori entre {x} i {y} és: {numero_aleatori}")