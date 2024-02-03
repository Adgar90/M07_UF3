"""
Funció que rep un diccionari amb una
llista de la compra (preu:descompte).

Demana a l'usuari l'IVA a aplicar al total
de la llista de la compra i mostra per pantalla
els valors amb el descompte aplicat més l'IVA.
"""

def calc_discount(productes):
    #Input d'IVA
    iva = int(input("introdueix l'IVA: "))
    #Comprovació d'IVA vàlid
    iva = iva if iva==4 or iva==10 else 21
    #Variable per mostrar l'index dels productes
    index = 1
    #Iteració key, value del dictionari que rep per paràmetre
    for price, disc in productes.items():
        #Càlcul del descompte
        discount = price * (disc / 100)
        #Preu amb descompte
        total_price = price - discount
        #Preu amb suma de l'IVA
        price_plus_iva = total_price + total_price*(iva/100)
        #Print del total
        print(f'Producte {index}:  {price_plus_iva}')
        #++ d'index
        index+=1