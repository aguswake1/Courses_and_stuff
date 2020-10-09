# Con la librería Jinja2 podemos crear webpages dinamicas
from jinja2 import FileSystemLoader, Environment
from wsgiref.simple_server import make_server


def application(environ, start_response):
    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template('template.html')

    data = {'title': 'WSGI tutorial', 'username': 'tumama'}
    html = template.render(data)
    headers = [('Content-type', 'text/html; charset=utf-8')]
    start_response('200 OK', headers)
    return [bytes(html, 'utf-8')]


server = make_server('localhost', 8000, application)
server.serve_forever()
# no funciona...
