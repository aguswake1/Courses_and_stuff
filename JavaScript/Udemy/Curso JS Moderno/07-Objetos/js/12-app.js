//object literal
const monitor = {
    nombre: 'Monitor 50 pulgadas',
    precio: 300,
    disponible: true,
}

//object constructor
function Productos(nombre, precio) {
    this.nombre = nombre;
    this.precio = precio;
    this.disponible = true;
}

const monitor2 = new Productos('monitor 20"', 100);