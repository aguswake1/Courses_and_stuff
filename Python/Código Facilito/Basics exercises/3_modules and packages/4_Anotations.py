# Las anotaciones son solamente informativas.
def saludo(nombre: str) -> None:  # especifica el tipo que retorna y el tipo del parámetro
    print("Hola " + nombre)
# Con la libreria typing podemos usar list, tuple, dict y otros


def suma(num1: int, num2: int = 100) -> int:
    return num1 + num2


nombre = "Eduardo"
saludo(nombre)
print(suma(10))
