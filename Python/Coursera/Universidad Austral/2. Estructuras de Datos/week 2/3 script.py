while True:
    try:
        x = int(input("Ingresa un numero pa: \n"))
        break
    except ValueError:
        print("mmm que ingresaste???")


def find(elemento, lista):
    """Devuelve el indice donde se encuentra el @elemento en la @lista.
    Si no lo encuentra devuelve -1.
    """
    index = 0

    while True:
        try:
            if lista[index] == elemento:
                return index
        except IndexError:
            return -1
        index += 1


find(4, [2, 3, 4, 5])  # Devuelve 2
find(1, [2, 3, 4, 5])  # Devuelve -1


def divide(num1, num2):
    """Divide dos números"""
    try:
        result = num1 / num2
    except ZeroDivisionError:
        print("División por cero!")
    else:
        print("El resultado es ", result)
    finally:
        print("Ejecutando finally (?")


divide(2, 1)
divide(2, 0)


# levantar excepciones
import math


def raizCuadrada(num):
    if num <= 0:
        raise ValueError("El número debe ser mayor a 0")
    return math.sqrt(num)


# creando tipos de excepciones en python, haciendo que se herede de la clase exceptions

class InvalidNumber(Exception):
    """lanza error de numero negativo"""
    pass


def raizCuadrada(num):
    if num <= 0:
        raise InvalidNumber("El número debe ser mayor a 0")
    return math.sqrt(num)
