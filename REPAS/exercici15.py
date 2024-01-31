mySet = set()
while True:
    num = input('Introdueix un número (0 per finalitzar): ')
    if int(num) == 0:
        print(tuple(sorted(mySet)))
        break
    mySet.add(int(num))