"""
Funció que rep una frase per paràmetre i que
la retorna en format diccionari. El contigut
serà { paraula:longitud }
"""

def frase_to_dict(frase):
    dict = {}
    for paraula in frase.split(" "):
        dict.update({paraula:len(paraula)})
    return dict
