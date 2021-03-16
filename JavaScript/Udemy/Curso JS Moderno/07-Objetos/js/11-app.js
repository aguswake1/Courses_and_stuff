const monitor = {
    nombre: 'Monitor 50 pulgadas',
    precio: 300,
    disponible: true,
    mostrarInfo: function () {
        console.log(`El producto ${this.nombre} vale ${this.precio}`);
    }
}
// usando el operador this
monitor.mostrarInfo();