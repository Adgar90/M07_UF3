text = input("Introdueix un text: ")
word = ""
for letter in text:
    if word.count(letter) < 1 or letter == " ":
        word += letter
tupla = tuple(word.split(" "))
print(tupla)