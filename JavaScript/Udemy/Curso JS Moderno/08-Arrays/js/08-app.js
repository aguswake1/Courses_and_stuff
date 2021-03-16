//destructuring array
const numeros = [10, 20, 30, 40, 50];
// obtenemos el elemento 30 en la variable tercero
const [, , tercero] = numeros;
// [30,40,50] asignados a tercero
const [primero, segundo, ...tercero] = numeros;