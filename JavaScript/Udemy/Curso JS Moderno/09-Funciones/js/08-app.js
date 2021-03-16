function sumar(a, b) {
    return a + b
}

const resultado = sumar(2, 3);


//ejemplo mas avanzado

let total = 0;

function agregarCarrito(precio) {
    return total += precio;
}

function calcularImpuestos(total) {
    return total * 1.15; // 15% impuesto
}

total = agregarCarrito(300);

const totalPagar = calcularImpuestos(total);

console.log(`El total a pagar es ${totalPagar}`);