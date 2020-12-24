a_list = [1, 2, 3, 4, 5]

# Devuelve el indice
a_list.index(4)
# Lanza una excepción del tipo valueError
a_list.index(6)

# mas argumentos: x, desde, hasta
a_list.index(4, 1)
a_list.index(4, 0, 2)
a_list.index(4, 1, 4)


b_list = [3, 1, 2, 9, 5, 4, 7, 8, 6]

# ordena los elementos de la lista
# ascendente
b_list.sort()
# descendente
b_list.sort(reverse=True)
# invierte la posición de los elementos de la lista
b_list.reverse()
# ordena los elementos y crea una lista nueva
sorted(b_list)
sorted(b_list, reverse=True)


b_list = [(1, 9), (1, 3), (1, 4), [1, 2]]
# lo ordena por el segundo elemento
b_list.sort(key=lambda x: x[1])
sorted(b_list, key=lambda x: x[1])
