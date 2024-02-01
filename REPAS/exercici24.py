#Importem JSON
import json

#Definim la ruta del fitxer
ruta = "REPAS/books.json"

#Funció que rep la ruta d'un fitxer JSON i el llegeix
def llegeixJSON(ruta):
    with open(ruta, "r") as file:
        arxiu = (json.load(file))
        print(json.dumps(arxiu, indent=2))

llegeixJSON(ruta)