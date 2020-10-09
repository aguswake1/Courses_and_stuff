"""La comunidad web Python ha creado un estándar llamado Web Server Gateway Interface (WSGI). Este estándar
nos permite crear programas los cuáles se pueden comunicar a traves de HTTP, es decir, a travez de internet.
-WSGI está inspirado en el estándar Common Gateway Interface (CGI)
-Cuando creamos un programa con el estándar WSGI, el programa podrá ser ejecutado en un servidor como Apache
o nginix"""
from wsgiref.simple_server import make_server  # importamos la función que genera el servidor


""" parametro environ es un diccionario que contiene variables wsgi relacionadas con la peticion al cliente
parámetro start_response es un callback que recibe dos arg --> status y encabezados de respuesta
"""


def application(environ, start_response):
    headers = [('Content-type', 'Text/plain; charset=utf-8')]

    start_response('200 OK', headers)

    # retornamos recurso (este caso string)
    return ['Hola gente de codigofacilito'.encode('utf-8')]


# 3 arg = direc del server, puerto, función handler
server = make_server('localhost', 8000, application)
# funcion handler: algo que es capaz de "recibir" un evento, un mensaje, etc y actuar en función al mismo.
server.serve_forever()

# Podemos ver el resultado desde 'http://localhost:8000/'
