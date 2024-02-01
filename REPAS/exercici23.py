#Importem JSON
import json

#Creem variable per guardar en format JSON
titles = ['Unlocking Android', 'Android in Action, Second Edition', 'Specification by Example', 'Flex 3 in Action']
covers = [
    'https://s3.amazonaws.com/AKIAJC5RLADLUMVRPFDQ.book-thumb-images/ableson.jpg',
    'https://s3.amazonaws.com/AKIAJC5RLADLUMVRPFDQ.book-thumb-images/ableson2.jpg',
    'https://s3.amazonaws.com/AKIAJC5RLADLUMVRPFDQ.book-thumb-images/adzic.jpg',
    'https://s3.amazonaws.com/AKIAJC5RLADLUMVRPFDQ.book-thumb-images/ahmed.jpg'
]
years = ['2009', '2011', '2011', '2009']
pages = ['416', '592','433','576']

#Funció que crea e insereix 4 'book' amb les seves propietats
def createJson():
    #Creem la llista per guardar els nostres objectes
    books = []
    #Iteració rang 4
    for i in range(0,4):
        #Creem i afegim un book en cada iteració
        books.append(
        { 
            "book": {
                "title":titles[i],
                "cover":covers[i],
                "year":years[i],
                "pages":pages[i]
            }
        })
    #Escrivim el nostre .json
    with open("REPAS/books.json", "w") as file:
        json.dump(books, file, indent=2)
    with open("REPAS/books.json", "r") as file:
        #Mostrem el value de books
        print(json.dumps(json.load(file), indent=2))

createJson()