euros = input('Introdueix un valor en euros: ')
iva = input("Indica el % d'IVA a aplicar (4%, 10% o 21%): ")

print(f"El valor indicat per l'usuari: {euros}€")
print(f"El % d'IVA demanat per l'usuari: {iva}%")
resultat = int(euros) + (int(euros)*int(iva))/100
print(f"El valor final amb l'IVA afegit és: {resultat}€")