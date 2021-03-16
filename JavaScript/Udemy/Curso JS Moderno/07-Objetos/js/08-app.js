"use strict" // buenas practicas, estricto, habilita nuevos metodos
const monitor = {
    nombre: 'Monitor 50 pulgadas',
    precio: 300,
    disponible: true
}

// object methods
// con freeze no se puede modificar el objeto en absoluto
Object.freeze(monitor); // ahi se comporta como una constante
// saber si realmente esta congelado
console.log(Object.isFrozen(monitor));
monitor.nombre = 'sddss'; // no va a funcionar