ftotal = int(input('Introdueix el preu de tot el carrito: '))

iva = 21
def amb_iva(ftotal, iva):
    ftotal = ftotal * iva/100 + ftotal   
    return ftotal 

print(amb_iva(ftotal, iva))