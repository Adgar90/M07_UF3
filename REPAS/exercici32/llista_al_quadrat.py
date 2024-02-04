"""
Funció que agafa una llista amb 10 números
i retorna una altra llista amb els seus
quadrats
"""

def llista_al_quadrat(llista):
    for i in range(1, len(llista)):
        llista[i] = llista[i]**2
    return llista
