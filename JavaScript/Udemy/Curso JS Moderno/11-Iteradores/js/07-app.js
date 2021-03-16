const pendientes = ['simbel', 'estudiar js', 'uba'];

const carrito = [{
        nombre: 'Monitor 20 Pulgadas',
        precio: 500
    },
    {
        nombre: 'Televisión 50 Pulgadas',
        precio: 700
    },
    {
        nombre: 'Tablet',
        precio: 300
    },
    {
        nombre: 'Audifonos',
        precio: 200
    },
    {
        nombre: 'Teclado',
        precio: 50
    },
    {
        nombre: 'Celular',
        precio: 500
    },
    {
        nombre: 'Bocinas',
        precio: 300
    },
    {
        nombre: 'Laptop',
        precio: 800
    },
];

//for of
for (let pendiente of pendientes) {
    console.log(pendiente);
}

for (let producto of carrito) {
    console.log(`${producto.nombre} - ${producto.precio}`);

}