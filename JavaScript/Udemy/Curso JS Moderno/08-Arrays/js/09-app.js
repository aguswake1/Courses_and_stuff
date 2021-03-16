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

for (let i = 0; i < carrito.length; i++) {
    console.log(`${carrito[i].nombre} - Precio ${carrito[i].precio}`);
}

//metodo para iterar en arrays

carrito.forEach(function (producto) {
    console.log(`${producto.nombre} - Precio ${producto.precio}`);
});