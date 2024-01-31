"""
Funció que crea un XML, crea les seves etiquetes i insereix text segons
les següents especificacions:
    a) Un root de nom students.
    b) Cinc childs (del root) amb nom student.
    c) Cada child student ha de tindre 4 subchilds:
        i)      name
        ii)     surname
        iii)    email
        iv)     dni
    d) Ha d’haver-hi un atribut (amb nom i valor) a dintre de cada element child “student”.
    e) El text de cada etiqueta serà de la vostra elecció.
"""
import xml.etree.ElementTree as ET
def creaXML():
    #Creem element root --> students
    students = ET.Element('students')
    #Creem els child del element root
    for i in range(1,6):
        #Creació child student
        student = ET.SubElement(students, 'student')

        #Creació child Name i assignació de valor
        name = ET.SubElement(student, "name")
        name.text = "Nom "+str(i)

        #Creació child Surname i assignació de valor
        surname = ET.SubElement(student, "surname")
        surname.text = "Cognom "+str(i)

        #Creació child Email i assignació de valor
        email = ET.SubElement(student, "email")
        email.text = "Email "+str(i)

        #Creació child Dni i assignació de valor
        dni = ET.SubElement(student, "dni")
        dni.text = "Dni "+str(i)

    ET.indent(students)
    ET.ElementTree(students).write('Students.xml')
    ET.dump(students)

creaXML()