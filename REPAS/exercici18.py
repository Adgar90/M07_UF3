words = input("Insert two words: ")

tupla = tuple(words.replace(" ", ""))
myDict = {}

for letter in tupla:
    if letter not in myDict.keys():
        myDict[letter] = tupla.count(letter)

for key in myDict:
    print(f'Lletra "{key}": {myDict[key]}')