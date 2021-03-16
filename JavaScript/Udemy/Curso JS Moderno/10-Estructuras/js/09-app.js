// operador ternario
const autenticado = true;
const puedePagar = true;

console.log(autenticado && puedePagar ? 'si, esta autenticado y puede pagar' : null);
// ternario anidado
console.log(autenticado ? puedePagar ? 'si, esta autenticado y puede pagar' : 'si esta autenticado pero no puede pagar' : null);