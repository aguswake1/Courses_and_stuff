const titulo = document.querySelector('.contenido-hero h1');
console.log(titulo.innerText); // si en el css visibility= hidden no lo va a encontrar
console.log(titulo.textContent);
console.log(titulo.innerHTML); //trae html

titulo.textContent = 'que onda pa';

const imagen = document.querySelector('.card img');
imagen.src = 'img/hacer2.jpg';