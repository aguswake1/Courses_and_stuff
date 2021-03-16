// eventos con mouse
const nav = document.querySelector('.navegacion');

nav.addEventListener('click', () => {
    console.log('clickeado');
});

nav.addEventListener('mouseenter', () => {
    console.log('sobre la nav');
    nav.style.backgroundColor = 'white';

});

nav.addEventListener('mouseout', () => {
    console.log('saliendo de la nav');
    nav.style.backgroundColor = 'transparent';
});
// doble click
nav.addEventListener('dblclick', () => {
    console.log('doble click');
    nav.style.backgroundColor = 'transparent';
});
//cuando soltas el click izquierdo
nav.addEventListener('mouseup', () => {
    console.log('soltando click');
    nav.style.backgroundColor = 'transparent';
});

//similar al click
nav.addEventListener('mousedown', () => {
    console.log('casi click');
    nav.style.backgroundColor = 'transparent';
});