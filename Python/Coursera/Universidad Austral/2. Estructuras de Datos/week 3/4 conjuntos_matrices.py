frutas = {'manzana', 'naranja', 'manzana', 'pera', 'naranja', 'banana', 'kiwi'}

'pera' in frutas
'yerba' in frutas

# conjunto vacio
set()

# otras formas de crear conjuntos
a = set('abracadabra')
b = set('alacazam')

# operaciones de conjuntos
a - b  # letras en a pero no en b
a | b  # letras en a o en b o en ambas
a & b  # letras en a y en b
a ^ b  # letras en a o b pero no en ambos

# comprensión de conjuntos
a = {x for x in 'abracadabra' if x not in 'abc'}

a.add('j')
a.remove('a')
