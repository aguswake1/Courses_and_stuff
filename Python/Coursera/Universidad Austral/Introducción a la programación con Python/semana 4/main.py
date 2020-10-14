"""
Tendrás que crear un programa que simule la tirada de dados.
Cada vez que ejecutamos el programa, este elegirá dos números aleatorios entre el 1 y el 6. El programa deberá imprimirlos en pantalla, imprimir su suma y preguntarle al usuario si quiere tirar los dados otra vez.

"""
import random
import time

tirar_devuelta = "si"

while tirar_devuelta == "si":
	dados = random.choices([1,2,3,4,5,6], k=2)
	suma = dados[0] + dados[1]
	print("Tus dados dieron: {} \n La suma de los mismos es de {}".format(dados,suma))
	time.sleep(2.5)
	tirar_devuelta = str(input("Desea lanzar los dados de nuevo? (ingrese 'si' o 'no')\n"))
