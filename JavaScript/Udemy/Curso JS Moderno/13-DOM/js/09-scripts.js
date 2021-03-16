//eliminar elementos
const primerEnlace = document.querySelector('a');
primerEnlace.remove();

//elimina desde el padre
const navegacion = document.querySelector('.navegacion');
navegacion.removeChild(navegacion.children[2])