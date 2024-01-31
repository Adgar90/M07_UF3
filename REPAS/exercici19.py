areas_pis = [
    "Menjador", 10.15, "Rebedor", 9.56,
    "Habitació1", 12.34, "Terrassa", 15.55,
    "Lavabo", 7.98, "Cuina", 12, "Habitació2", 12.23
]

#Imprimir segon element
print(areas_pis[1:2])
#Imprimir l'últim element
print(areas_pis[-1:])
#Imprimir l'àrea de la terrassa
print(areas_pis[areas_pis.index("Terrassa")+1:areas_pis.index("Terrassa")+2])
#Imprimir del primer element al tercer element
print(areas_pis[:3])
#Imprimir del tercer element a l'últim
print(areas_pis[3:])
#Imprimir el total de l'àrea de les dues habitacions
print(areas_pis[areas_pis.index("Habitació1")+1]+areas_pis[areas_pis.index("Habitació2")+1])
#Modificar l'àrea del lacabo i imprimir la nova list area
print()
#Afegir l'àrea de "pati interior" i 2.78 a les últimes posicions. Imprimir la nova list
print()
#Imprimir el total de l'àrea del pis
print()