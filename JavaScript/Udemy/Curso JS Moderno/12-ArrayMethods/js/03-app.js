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

// con un foreach averiguar precio total del carrito
let total = 0;
carrito.forEach(producto => total += producto.precio)

// con un reduce
// el 0 es la inicializacion de total
let resultado = carrito.reduce((total, producto) => total + producto.precio, 0)