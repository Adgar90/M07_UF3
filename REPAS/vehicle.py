#Class Vehicle
class Vehicle:
    #Constructor de vehícle (self + 6 atributs)
    def __init__(self, marca, model, color, rodes, cavalls, vel_maxima):
        self.marca = marca
        self.model = model
        self.color = color
        self.rodes = rodes
        self.cavalls = cavalls
        self.vel_maxima = vel_maxima
    
    #Getters
    def get_marca(self):
        return self.marca
    def get_model(self):
        return self.model
    def get_color(self):
        return self.color
    def get_rodes(self):
        return self.rodes
    def get_cavalls(self):
        return self.cavalls
    def get_vel_maxima(self):
        return self.vel_maxima
    
    #Setters
    def set_marca(self, new_marca):
        self.marca = new_marca
    def set_model(self, new_model):
        self.model = new_model
    def set_color(self, new_color):
        self.color = new_color
    def set_rodes(self, new_rodes):
        self.rodes = new_rodes
    def set_cavalls(self, new_cavalls):
        self.cavalls = new_cavalls
    def set_vel_maxima(self, new_vel_maxima):
        self.vel_maxima = new_vel_maxima

    #Funció per mostrar totes les dades del vehicle
    def parts(self):
        return f"""
            Marca: {self.marca}
            Model: {self.model}
            Color: {self.color}
            Rodes: {self.rodes}
            Cavalls: {self.cavalls} cv
            Velocitat Máxima: {self.vel_maxima} km / h
        """
    
    #Funció per convertir l'objecte en format json
    def to_dict(self):
        return {
            "marca":self.marca,
            "model":self.model,
            "color":self.color,
            "rodes":self.rodes,
            "cavalls":self.cavalls,
            "vel_maxima":self.vel_maxima
        }
    
#Inicialització d'una instància
vehicle = Vehicle( "Audi", "Q7","White", 4, 232, 200)

#Prints de comprovació
print(vehicle.parts())
print(vehicle.to_dict())