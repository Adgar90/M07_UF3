word1 = input("Insert first word: ")
word2 = input("Insert second word: ")

tupla = tuple(word1)
tupla += tuple(word2)

myDict = {}

for letter in tupla:
    if letter not in myDict.keys():
        myDict[letter] = tupla.count(letter)

for key in myDict:
    print(f'Lletra "{key}": {myDict[key]}')