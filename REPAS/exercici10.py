import random

rand = random.randint(1, 100)
intents = 0
while True:
    number = input("Introdueix un número del 1 al 100 ")
    if (int(number) < rand):
        print("El número a endevinar és més gran")
    elif (int(number) > rand):
        print("El número a endevinar és més petit")
    else:
        print("Has encertat. El número era "+str(rand))
        break
    intents+=1
    print("Intents: "+str(intents))