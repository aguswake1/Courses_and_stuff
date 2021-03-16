const meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio'];

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

// comprobar si un valor existe en un arreglo
// esta bien para una entrevista pero para el mundo real no
meses.forEach(mes => {
    if (mes === 'Enero') {
        console.log('enero existe');
    }
});

// array method
const resultado = meses.includes('Enero'); //devuelve un bool


// en un arreglo de objetos se usa .some
const existe = carrito.some(producto => producto.nombre === 'Teclados') //devuelve bool

// arreglo tradicional con .some
const existe2 = meses.some(mes => mes === 'Monitor Curvo');