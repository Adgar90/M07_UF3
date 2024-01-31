numbers = input("Introdueix 10 números separats per un espai: ")

tupla = tuple(numbers.split(' '))
tupla = tuple(sorted(tupla))
print(tupla)