# creo lista
animals= ['man', 'bear', 'pig']
# imprimo el primer elemento
print(animals[0])
# cambio el valor del primer elemento
animals[0] = 'cat'
# añado al final un elemento 
animals.append('dog')
# imprimo el último elemento de la lista
print(animals[-1])

print(animals)

#Añadir varios elementos a una lista, con una lista

lista_aux = ['horse', 'caterpilar', 'duck']
animals.extend(lista_aux)
print(animals)
# insert method adds an element in an especific position
animals.insert(3, 'cow')
print(animals)

# slices del elemento seleccionado:elemento seleccionado -1

print(animals[1:4])   
print(animals[:2])  # del cero al 2 (primeros dos)
print(animals[-2:])  # ultimos dos 
print('horse'[1:3])

#Averiguar la posicion de un elemento

print(animals.index('cat'))

# Evitar que Python lance un error
try:
    print(animals.index('truck'))
except:
    print("No pudimos encontrar lo que buscaba :(")

# loops

for animal in animals:
    print(animal)

i = 0
while (len(animals) > 0):
    print(animals[i])
    animals.remove(i)
    i += 1
    
    
