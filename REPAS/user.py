#Class User
class User:
    #Constructor amb 6 atributs
    def __init__(self, nom, cognom, edat, email, dni, telefon):
        self.nom = nom
        self.cognom = cognom
        self.edat = edat
        self.email = email
        self.dni = dni
        self.telefon = telefon
    #Getters
    def get_nom(self):
        return self.nom
    def get_cognom(self):
        return self.cognom
    def get_edat(self):
        return self.edat
    def get_email(self):
        return self.email
    def get_dni(self):
        return self.dni
    def get_telefon(self):
        return self.telefon
    #Setters
    def set_nom(self, new_nom):
        self.nom = new_nom
    def set_cognom(self, new_cognom):
        self.cognom = new_cognom
    def set_edat(self, new_edat):
        self.edat = new_edat
    def set_email(self, new_email):
        self.email = new_email
    def set_dni(self, new_dni):
        self.dni = new_dni
    def set_telefon(self, new_telefon):
        self.telefon = new_telefon
    #Mètode salutació() per mostrar les dades del user
    def salutacio(self):
        return f"""
            Nom: {self.nom}
            Cognom: {self.cognom}
            Edat: {self.email}
            Email: {self.email}
            DNI: {self.dni}
            Telèfon: {self.telefon}
        """
    #Funció per convertir l'objecte en format json
    def to_dict(self):
        return {
            "nom":self.nom,
            "cognom":self.cognom,
            "edat":self.edat,
            "email":self.email,
            "dni":self.dni,
            "telefon":self.telefon
        }