"""
Funció que rep la quantitat de la factura
i l'IVA a aplicar (4%, 10% o 21%). En cas
de no passar-li cap valor o un valor erroni
s'aplicarà el 21%.

Mostrarà per pantalla el valor sense IVA,
l'IVA i el total.
"""
def calcula_iva(base, iva):
    iva = iva if iva==4 or iva==10 else 21
    base_mes_iva = int(base + base*(iva/100))
    print(f'Valor base: {base}')
    print(f"L'IVA a aplicar: {iva}%")
    print(f"Base amb l'IVA aplicat: {base_mes_iva}")