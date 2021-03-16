const usuario = true;
const puedePagar = true;

if (usuario && puedePagar) {
    console.log('eres usuario y puedes pagar');
} else if (!usuario) {
    console.log('registrate primero!');
} else if (!puedePagar) {
    console.log('fondos insuficientes');
}