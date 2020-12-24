a_list = [3, 7.56, 'hola', 7j + 5, [1, 2]]

# Acceso mediante indexación
a_list[0]  # 3
a_list[2]  # hola
a_list[-1]  # [1, 2]

# Slicing
a_list[1:]  # [7.56, 'hola', 7j + 5, [1, 2]]
a_list[1:2]  # [7.56]
a_list[1:3]  # [7.56, 'hola']
a_list[:2]  # [3, 7.5]
a_list[:]  # [3, 7.56, 'hola', 7j + 5, [1, 2]]

# Algunas funciones

# Devuelve la cantidad de elementos en una lista
len(a_list)  # 5
# Agrega un elemento al final de la lista
a_list.append(2)
# Extiende la lista con los elementos de otra lista
a_list.extend(['buen dia', 5])
# Inserta un elemento en una posición determinada
a_list.insert(4, 'intercalado')
a_list.insert(12, 'Out of range')
a_list.insert(-1, 'backwards')
# Cuenta la cantidad de veces que el parámetro aparece en la lista
a_list.count(3)
# Elimina el primer elemento que coincida con el parámetro
a_list.remove(3)
# Hace una copia superficial de la lista
a_list_aux = a_list.copy()
# Saca el último elemento de la lista y lo devuelve
a_list.pop()
# Saca el elemento indicado en parámetro y lo Devuelve
a_list.pop(3)
""" Borra toda la lista, si estamos almacenando en una variable algo de
esta lista, es importante que usemos esta función en lugar de = [] porque
modificaria nuestra variable"""
a_list.clear()


# listas y strings
nombre = 'Agustin'
lista = list(nombre)

# El indexado funciona de igual manera
nombre[0]
lista[0]

# El slicing funciona de igual manera
nombre[:4]
lista[:4]

# La función len funciona de igual manera
len(nombre)
len(lista)

# El in funciona en ambas
'A' in nombre
'A' in lista

# El not in funciona en ambas
'z' not in nombre
'z' not in lista

# Los string también se pueden recorrer con un for
for letra in nombre:
    print(letra)

# Los strings son inmutables
lista[2] = 'o'
nombre[2] = 'o'  # TypeError


""" Listas como pilas LIFO (Last In First Out) lo
simulamos con la función append y pop"""
stack = [1, 2, 3]

stack.append(5)
stack.pop()


# Listas como colas FIFO (First In First Out)
stack.append(5)
stack.pop(0)

# Necesitamos hacer uso de una librería para que sea mas eficiente
from collections import deque
queue = deque(stack)
queue.append(5)
queue.popleft()

# List comprehension
# lista de cuadrados
cuadrados = []
for x in range(10):
    cuadrados.append(x**2)

# lista por comprensión
cuadrados_2 = [x**2 for x in range(10)]

# cuadrados usando la funcion map
cuadrados_3 = list(map(lambda x: x**2, range(10)))

listoide = [-4, -2, 0, 2, 4]

# lista por comprensión con los numeros positivos de listoide
positivos = [x for x in listoide if x >= 0]

# List compr. con los numeros positivos de listoide con funcion filter
positivos_2 = list(filter(lambda x: x > 0, listoide))

# numeros pares y su cuadrado
[(x, x**2) for x in range(6)]

# lista de pares combinados
pares = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]

# equivale a
pares_2 = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            pares_2.append((x, y))
