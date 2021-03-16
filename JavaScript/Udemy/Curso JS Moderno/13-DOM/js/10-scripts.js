// crear elementos
const enlace = document.createElement('a');
enlace.textContent = 'nuevo enlace';
enlace.href = '#';
enlace.target = '_blank';
enlace.classList.add('nueva-clase');
enlace.setAttribute('data-enlace', 'nuevo-enlace');
enlace.onclick = miFuncion;

//seleccionar navegacion
const navegacion = document.querySelector('.navegacion');
navegacion.appendChild(enlace); //agregarlo
//console.log(navegacion.children);
navegacion.insertBefore(enlace, navegacion.children[1]); //agregarlo especificamente| (lo que deseamos agregar, donde lo deseamos)

function miFuncion() {
    alert('diste click');
}

// crear un CARD

const parrafo1 = document.createElement('p');
parrafo1.textContent = 'Concierto';
parrafo1.classList.add('categoria', 'concierto');

const parrafo2 = document.createElement('p');
parrafo2.textContent = 'Concierto de rock';
parrafo2.classList.add('titulo');

const parrafo3 = document.createElement('p');
parrafo3.textContent = '800 por persona';
parrafo3.classList.add('precio');


const info = document.createElement('div');
info.classList.add('info');
info.appendChild(parrafo1);
info.appendChild(parrafo2);
info.appendChild(parrafo3);

// crear la imagen

const imagen = document.createElement('img');
imagen.src = 'img/hacer2.jpg';
imagen.classList.add('img-fluid');
imagen.alt = 'texto alternativo';

// crear card
const card = document.createElement('div');
card.classList.add('card');

//asignar imagen
card.appendChild(imagen);

//asignar info
card.appendChild(info);

//insertar en el html

const contenedor = document.querySelector('.hacer .contenedor-cards');
contenedor.insertBefore(card, contenedor.children[0]);