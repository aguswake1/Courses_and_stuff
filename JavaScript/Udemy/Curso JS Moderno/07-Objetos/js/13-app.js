const monitor = {
    nombre: 'Monitor 50 pulgadas',
    precio: 300,
    disponible: true,
}
// devuelve parte de la izquierda
console.log(Object.keys(monitor));
// devuelve parte de la derecha
console.log(Object.values(monitor));
// devuelve todo
console.log(Object.entries(monitor));