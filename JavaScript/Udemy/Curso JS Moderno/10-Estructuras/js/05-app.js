//switch case
const metodoPago = 'efectivo'
switch (metodoPago) {
    case 'efectivo':
        console.log(`Pagaste con ${metodoPago}`);
        break;
    default:
        console.log('Metodo de pago no soportado');
        break;
};