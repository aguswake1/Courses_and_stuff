//una variable declarada en const se puede modificar si es un objeto o a un arreglo
const meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio'];

meses[0] = 'hola';
// se saltea las demas posiciones y crea un elemento en la posicion 20
meses[20] = 'aaja';