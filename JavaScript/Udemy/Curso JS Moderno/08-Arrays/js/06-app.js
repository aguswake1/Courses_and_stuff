// FORMA DECLARATIVA ES6 -- crea nuevo elemento
//sintaxis mas confusa

const carrito = [];

const producto = {
    nombre: 'celular',
    precio: 800
};

const producto2 = {
    nombre: 'monitor',
    precio: 800
};

const producto3 = {
    nombre: 'pizza',
    precio: 800
};

let resultado;
// pizza-celular-monitor
resultado = [...carrito, producto];
resultado = [...resultado, producto2];
resultado = [producto3, ...resultado];



console.table(resultado);