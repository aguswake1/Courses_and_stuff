# WEB PAGE
from wsgiref.simple_server import make_server


HTML = """
<!DOCTYPE html>
<html>
    <head>
        <title>Hola</title>
    </head>
    <body><h1>Buenos días :)</h1></body>
</html>
"""


def application(environ, start_response):
    headers = [('Content-type', 'Text/html; charset=utf-8')]

    start_response('200 OK', headers)

    return [bytes(HTML, 'utf-8')]


server = make_server('localhost', 8000, application)

server.serve_forever()
