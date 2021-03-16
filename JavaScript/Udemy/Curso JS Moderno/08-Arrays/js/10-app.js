const carrito = [{
    nombre: 'cocina',
    precio: 200
}, {
    nombre: 'monitor',
    precio: 800
}, {
    nombre: 'celular',
    precio: 1200
}];

//metodo para iterar en arrays
carrito.forEach(function (producto) {
    console.log(`${producto.nombre} - Precio ${producto.precio}`);
});

// la funcion map funciona igual pero devuelve un nuevo carrito
const nuevoCarrito = carrito.map(function (producto) {
    return `${producto.nombre} - Precio ${producto.precio}`;
});