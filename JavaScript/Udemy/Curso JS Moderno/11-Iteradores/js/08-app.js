const pendientes = ['simbel', 'estudiar js', 'uba'];

const automovil = {
    modelo: 'camaro',
    year: 1969,
    motor: '6.0'
}
// for in para objetos
for (let propiedad in automovil) {
    console.log(`${automovil[propiedad]}`);
}

for (let [llave, valor] of Object.entries(automovil)) {
    console.log(valor);
    console.log(llave);

}