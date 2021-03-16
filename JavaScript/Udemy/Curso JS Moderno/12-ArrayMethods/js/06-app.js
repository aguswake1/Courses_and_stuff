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

// todos los productos deben cumplir la condicion para que devuelva true
const resultado = carrito.every(producto => producto.precio < 1000);

// al menos un producto debe cumplir la condicion para que devuelva true
const resultado2 = carrito.some(producto => producto.precio < 500);