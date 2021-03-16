// hoisting
sumar(); //funciona

// declaracion de funcion ( function declaration)
function sumar() {
    console.log(2 + 2);
}


sumar2(); // no funciona

//expresion de funcion (function expression)
const sumar2 = function () {
    console.log(3 + 3);
}