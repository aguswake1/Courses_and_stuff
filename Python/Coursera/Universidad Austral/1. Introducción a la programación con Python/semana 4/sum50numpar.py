#Sumatoria de los primeros 50 números pares
"""
def sumPar(num):
	resultado = 0
	for x in range(2,num*2 + 1,2):
		print(x)
		resultado += x

	return resultado


print(sumPar(50))
"""

class SumaDos:
	def __init__(self, datos):
		self.datos = datos
		self.indice = 0

	def __iter__(self):
		return self

	def __next__(self):
		if self.indice == len(self.datos):
			raise StopIteration()
			elemento = self.datos[self.indice] + 2
			self.indice +=1
			return elemento


list(SumaDos([1,2,3,4,5]))