"""
Funció que retorna tots el números que hi ha
entre els dos números que li passem per paràmetre.
També mostrarà la suma d'aquests números.
"""
def mostra_nums(x, y):
    #Variable on guardarem la suma total del numeros
    suma_total = 0
    #Iteració amb ternaria per sempre fer range de menor a major
    for i in range(x, y+1) if x<y else range(y,x+1):
        suma_total += i
        print(i)
    print(f'La suma total és: {suma_total}')