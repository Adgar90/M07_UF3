word1 = input("Introdueix primera paraula: ")
word2 = input("Introdueix segona paraula: ")

result = word2[0]+word1[1:]+" "+word1[0]+word2[1:]
print(result)
