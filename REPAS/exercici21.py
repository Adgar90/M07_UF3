#Demanar 10 números separats per espais
numbers = input("Introdueix 10 números separats per espais: ")

#Afegir els números a una llista
llista_numeros = numbers.split(" ")

#Mostrar els números de l'usuari
print(f"Números de l'usuari: {llista_numeros}")
#Sumar tots el números
sum_total = 0
for num in llista_numeros:
    sum_total+=int(num)
print(f'Suma total: {sum_total}')
#Mitjana
mitjana = sum_total/len(llista_numeros)
print(f'Mitjana: {mitjana}')