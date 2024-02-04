
"""
Funció que rep una funció i una llista.

Crea una nova llista i amb la funció quadrat(x),
guardarà els nous valors.
"""
def llista_quadrat(quadrat, llista):
    llista_al_quadrat = []
    for x in llista:
        llista_al_quadrat.append(quadrat(x))
        print(quadrat(x))
    print(llista_al_quadrat)
#Funció que retorna el número que rep elevat al quadrat
def quadrat(x):
    return x**2