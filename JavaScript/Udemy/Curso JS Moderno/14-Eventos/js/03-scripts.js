const busqueda = document.querySelector('.busqueda');

// funca cuando se presiona cualquier tecla
busqueda.addEventListener('keydown', () => {
    console.log('escribiendou');
})

// funca cuando se suelta la tecla presionada
busqueda.addEventListener('keyup', () => {
    console.log('escribiendou');
})

// excelente para validaciones
// una vez que se ingresa y se sale de un input
busqueda.addEventListener('blur', () => {
    console.log('validado');
})

// ctrl c
busqueda.addEventListener('copy', () => {
    console.log('copiaste');
})

// ctrl v
busqueda.addEventListener('paste', () => {
    console.log('pegaste');
})
//ctrl x
busqueda.addEventListener('cut', () => {
    console.log('cortaste');
})


// cubre los anteriores menos el blur y creo que copiar
busqueda.addEventListener('input', e => {
    console.log(e.type);
    // saber lo que el usuario escribe
    console.log(e.target.value);

})