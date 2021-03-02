const producto = "Monitor 20 pulgadas";

//reemplazar la palabra por:
console.log(producto.replace('pulgadas', '"'));
console.log(producto.replace('Monitor', 'Monitor curvo'));

// cortar de tal index a tal otro
console.log(producto.slice(0, 10));
// con un solo parámetro recorta hasta el final
console.log(producto.slice(2));
// debido a que no puede recortar para atras, no hace nada
console.log(producto.slice(2, 1));

console.log(producto.substring(0, 10));
// debido a que está al reves lo invierte (1,2)
console.log(producto.substring(2, 1));

// obtener la letra A
const usuario = "Agustin";
console.log(producto.substring(0, 1));
console.log(producto.charAt(0));