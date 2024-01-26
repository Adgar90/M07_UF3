import sys
meses = (
    'Enero',
    'Febrero',
    'Marzo',
    'Abril',
    'Mayo',
    'Junio',
    'Julio',
    'Agosto',
    'Septiembre',
    'Octubre',
    'Noviembre',
    'Diciembre'
)
while True:
    pos = input("Posa un número entre 0 i 12: ")
    if int(pos) == 0:
        break
    print(meses[(int(pos)-1)])