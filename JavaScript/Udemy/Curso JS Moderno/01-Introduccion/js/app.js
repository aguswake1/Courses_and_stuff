// alert("Hola mundo");
/*
======================================
===LE PREGUNTA AL USUARIO SU NOMBRE===
======================================
*/
const nombre = prompt("¿Cómo te llamas?");
document.querySelector(".contenido").innerHTML = `${nombre} está aprendiendo JavaScript`;

/*
TIPS CONSOLA
console.clear();  // limpia la consola
console.log("hola");
console.error("hola");
console.warn("hola");

// ver que código es mas óptimo
console.time("codigoPrueba");
--codigo--
console.timeEnd("codigoPrueba");
*/