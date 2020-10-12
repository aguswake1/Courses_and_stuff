
class Animal:  # Clase padre
	def comer(self):
		print("Comiendo")

	def dormir(self):
		print("Durmiendo")

class mascota(): # Clase padre
	def fecha_adopcion(self, fecha):
		self.fecha_de_adopcion = fecha


class Perro(Animal, mascota):  # Aplicando herencia múltiple
	def __init__(self, nombre):
		self.nombre = nombre

	def ladrar(self):
		print("Ladrando ")

class Gato(Animal, mascota):  # Aplicando herencia múltiple
	def __init__(self,nombre):
		self.nombre = nombre

	def ronronear(self):
		print("ronroneando")
	
	def comer(self):
		print(self.nombre,"no está Comiendo")  #Overwrite | sobrescritura de métodos
		Animal.comer(self)

Ema = Perro("Ema")  # Instanciamos
Ema.ladrar()
Ema.dormir()
Ema.comer()

Manchas = Gato("Manchas")  # Instanciamos
Manchas.ronronear()
Manchas.dormir()
Manchas.comer()
Manchas.fecha_adopcion("ayer")
print(Manchas.fecha_de_adopcion)

# Siempre debemos colocar las clases padres arribas de las que heredan
# Si hay un método con el mismo nombre, se ejecuta el de la clase heredada, no la del molde