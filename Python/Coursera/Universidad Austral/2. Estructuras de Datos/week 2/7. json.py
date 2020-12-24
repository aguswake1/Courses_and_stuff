import json

# serializar un objeto
json.dumps([1, 2, 3])

# desearizar un objeto
json.loads('[1, 2, 3]')

# Escribir como json directamente a un archivo
with open('path_to_file', 'w') as a_file:
    json.dump([1, 2, 3], a_file)

# Leer un json directamente desde un archivo
with open('path_to_file', 'r') as a_file:
    a_list = json.load(a_file)
