// objeto dentro de objetos
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

console.log(monitor.informacion.medidas.peso);