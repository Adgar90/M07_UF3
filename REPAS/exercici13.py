number = input('Introdueix un número del 1 al 10: ')
taula = number+", "
for i in range(2, 11):
    if i < 10:
        taula+= (str(i*int(number))+", ")
    else:
        taula+= ("i "+str(i*int(number)))

print(taula)