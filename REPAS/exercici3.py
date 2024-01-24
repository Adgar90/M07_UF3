valor1 = input('Primer valor: ')
valor2 = input('Segon valor: ')

valor1 = int(valor1)
valor2 = int(valor2)

if valor1>valor2:
    print(f'{valor1} és més gran que {valor2}')
elif valor1<valor2:
    print(f'{valor1} és més gran que {valor2}')
else:
    print(f'{valor1} i {valor2} són iguals')