valor = input('Introdueix un número per saber si és parell o senar: ')

valor = int(valor)

if valor % 2 == 0:
    print(f'{valor} és parell')
else:
    print(f'{valor} és senar')