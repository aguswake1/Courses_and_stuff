class Gato:
	def __init__(self, name):  # clases padres con inicializadores
		self.name = name
	def __str__(self):
		return self.name;

class Pato(object):  # By default, classes inherit from 'object'.
	def __init__(self, name):
		self.name = name
		
	def __str__(self):
		return self.name;


gato = Gato("manchitas")
pato = Pato("donald")

print(gato, pato.__dict__)  # El método .dict muestra los atributos del objeto en forma de diccionario

# clase = molde  objeto = hijo atributos = características métodos = acciones
#metaprogramación