import modulo

print(modulo.suma(20, 5))


""" Distintas formas de importar
from modulo import *  ------------->  print(suma(20, 5))
from modulo import suma, resta
from modulo import suma as sm
from modulo import (suma,
					resta,
					division) """


if __name__ == '__main__':
	print("hola")
else:
	print("wtf")
