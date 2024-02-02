from user import User
from vehicle import Vehicle

#Inicialització d'una instància de vehicle i una d'User
vehicle = Vehicle( "Audi", "Q7","White", 4, 232, 200)
user = User("Adria", "Garcia", 33, "adri@iticbcn.cat", "12345678Y", "661223344")

#Prints de comprovació
print(vehicle.parts())
print(user.salutacio())
print(vehicle.to_dict())
print(user.to_dict())