# un módulo es un archivo donde definimos funciones o clases para reutilizar código

def suma(val1, val2):
	return val1 + val2


def resta(val1, val2):
	return val1 - val2


def division(val1, val2):
	return val1 * val2


def multiplicacion(val1, val2):
	return val1 / val2


dir(modulo)  # Esta función lo que hace es mostrarnos los objetos que hay en el archivo
# el atributo __name__ SIEMPRE es __main__ si es el archivo que ejecutamos, en este caso no lo es
# ejecutando main.py, el atributo __name__ de este archivo es "modulo"
