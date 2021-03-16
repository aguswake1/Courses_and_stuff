const monitor = {
    nombre: 'Monitor 50 pulgadas',
    precio: 300,
    disponible: true
}

const medidas = {
    peso: '1kg',
    longitud: '50cm'
}

//unir dos objetos
// forma num 1
const resultado = Object.assign(monitor, medidas);

// form num 2 spread/rest operator
const resultado2 = {
    ...monitor,
    ...medidas
};