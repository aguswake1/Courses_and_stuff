"""
lista = []

for x in range(0, 101):
    lista.append(x)

print(lista)"""

# es lo mismo que:

list_comprehension = [x for x in range(0, 101)]
print(list_comprehension)

tupla_comprehension = tuple((x for x in range(0, 101) if x % 2 == 0 if x < 50))  # numeros pares hasta 50
print(tupla_comprehension)

diccionario_comprehension = {indice: valor for indice, valor in enumerate(tupla_comprehension)}
print(diccionario_comprehension)
