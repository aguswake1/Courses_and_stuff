const carrito = [{
        nombre: 'Monitor 27 Pulgadas',
        precio: 500
    },
    {
        nombre: 'Televisión',
        precio: 100
    },
    {
        nombre: 'Tablet',
        precio: 200
    },
    {
        nombre: 'Audifonos',
        precio: 300
    },
    {
        nombre: 'Teclado',
        precio: 400
    },
    {
        nombre: 'Celular',
        precio: 700
    },
]

let resultado;
// mete todos los productos que sean mayor a 400
resultado = carrito.filter(producto => producto.precio > 400);
//simulacion de que borramos del carrito audifonos
resultado = carrito.filter(producto => producto.nombre !== 'Audifonos');