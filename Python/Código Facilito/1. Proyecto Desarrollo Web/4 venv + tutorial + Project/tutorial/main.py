# importar flask sirve para levantar el server
# render_template sirve para el renderizado de los templates
# request hace que podamos obtener los datos de la Querys string (?=)
from flask import Flask, render_template, request

app = Flask(__name__)


@app.before_request
def before_request():  # funcion que se ejecuta antes de la petición
    print("Antes de la petición")

# callbacks


@app.after_request
def after_request(response):  # funcion que se ejecuta despues de la petición
    """El parámetro es el return de otras funciones"""
    print("Después de la petición")
    return response


@app.route('/')  # decoradores
def index():
    """Definimos variables a utilizar en HTML"""
    name = 'Agustin Olano'
    coscu_rules = True
    lista = ["Python", "JS", "PHP", "Perl"]
    return render_template('index.html', username=name,
                           coscu_rules=coscu_rules,
                           lista=lista)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/users/<username>/<int:age>')  # by default parámetro tipo string
def user(username, age):
    return "Hola " + username + str(age)


@app.route('/data')
def data():
    """ args es un dict. podemos usar metodo get para obtener parametros.
    lo segundo es lo que devuelve si no encuentra la variable"""
    # /data?name=pepino --> return hola pepino
    name = request.args.get('name', '')
    # concantenar params ...=pepino&password=x
    password = request.args.get('password', 'intente nuevamente')
    return "hola " + name + ", su contraseña es " + password


if __name__ == '__main__':
    # si queremos otro servidor ponemos e.g. port=9000
    app.run(debug=True, port=9000)

"""Anotaciones: variables--> {{variable}}
instrucciones {% instrucciones %}
comentarios --> {# comentario #}
En jinja2 solo se permite el for como ciclo

Ejemplo con funciones:
def suma(val1,val2):
    return val1 + val2
def suma_template():
    return render_template('suma.html', val1=10, val2=20, funcion=suma)
template html--> {{funcion(val1,val2)}}


Query string es lo que se encuentra en la url de un metodo get despues del
signo de interrogacion"""
