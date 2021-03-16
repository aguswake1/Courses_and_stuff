const monitor = {
    nombre: 'Monitor 50 pulgadas',
    precio: 300,
    disponible: true,
    informacion: {
        medidas: {
            peso: '1kg',
            longitud: '50cm'
        },
        fabricacion: {
            pais: 'China'
        }
    }
}
//destructuring
// hay que definir cada variable exaustivamente
const {
    nombre,
    informacion: {
        medidas: {
            peso
        }
    },
    informacion
} = monitor;