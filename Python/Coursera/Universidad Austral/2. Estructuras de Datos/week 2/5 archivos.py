# Abrir archivo
a_file = open('/Users/Agustin Olano/Desktop/Informática/Courses_and_stuff/Python/Coursera/Universidad Austral/2. Estructuras de Datos/week 2/1 Excepciones.txt', 'r')

# Leer todo el contenido del archivo
a_file.read()

# Cerrar archivo
a_file.close()

# Abrir un archivo como context manager con la sentencia with
with open('/Users/Agustin Olano/Desktop/Informática/Courses_and_stuff/Python/Coursera/Universidad Austral/2. Estructuras de Datos/week 2/1 Excepciones.txt', 'r') as a_file:
    a_file.read()


# La función read lee todo el contenido del archivo
with open('/Users/Agustin Olano/Desktop/Informática/Courses_and_stuff/Python/Coursera/Universidad Austral/2. Estructuras de Datos/week 2/1 Excepciones.txt', 'r') as a_file:
    print(a_file.read())

# La función readline lee la linea actual del archivo
with open('/Users/Agustin Olano/Desktop/Informática/Courses_and_stuff/Python/Coursera/Universidad Austral/2. Estructuras de Datos/week 2/1 Excepciones.txt', 'r') as a_file:
    print(a_file.readline())

# La función readlines guarda en una lista las lineas del archivo
with open('/Users/Agustin Olano/Desktop/Informática/Courses_and_stuff/Python/Coursera/Universidad Austral/2. Estructuras de Datos/week 2/1 Excepciones.txt', 'r') as a_file:
    print(a_file.readlines())

# El ciclo for recorre linea a linea
with open('/Users/Agustin Olano/Desktop/Informática/Courses_and_stuff/Python/Coursera/Universidad Austral/2. Estructuras de Datos/week 2/1 Excepciones.txt', 'r') as a_file:
    for line in a_file:
        print(line)



# Escribe un string en el archivo, borra lo escrito previamente
with open('/Users/Agustin Olano/Desktop/Informática/Courses_and_stuff/Python/Coursera/Universidad Austral/2. Estructuras de Datos/week 2/1 Excepciones.txt', 'w') as a_file:
    print(a_file.write("Hola mundo"))

# Borra lo escrito previamente y escribe en 3 lineas diferente mediante una lista
with open('/Users/Agustin Olano/Desktop/Informática/Courses_and_stuff/Python/Coursera/Universidad Austral/2. Estructuras de Datos/week 2/1 Excepciones.txt', 'w') as a_file:
    print(a_file.writelines(["linea1\n", "linea2\n", "linea3\n"]))

# Se añade una linea mostrando el string
with open('/Users/Agustin Olano/Desktop/Informática/Courses_and_stuff/Python/Coursera/Universidad Austral/2. Estructuras de Datos/week 2/1 Excepciones.txt', 'a') as a_file:
    print(a_file.write("Hola mundo"))
