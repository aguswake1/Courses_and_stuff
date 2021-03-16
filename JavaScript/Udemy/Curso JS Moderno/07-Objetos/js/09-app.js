"use strict" // buenas practicas, estricto, habilita nuevos metodos
const monitor = {
    nombre: 'Monitor 50 pulgadas',
    precio: 300,
    disponible: true
}

// object methods
// con seal el objeto se puede modificar el contenido pero ni borrar ni agregar
Object.seal(monitor); // ahi se comporta como una constante
// saber si realmente esta sellado
console.log(Object.isSealed(monitor));
monitor.nombre = 'sddss'; // funciona