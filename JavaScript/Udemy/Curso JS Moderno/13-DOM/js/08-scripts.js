//traversing the dom
const navegacion = document.querySelector('.navegacion');

console.log(navegacion.childNodes); // los espacios en blanco son considerados elementos
console.log(navegacion.children);


console.log(navegacion.children[1].nodeName); // la etiqueta
console.log(navegacion.children[1].nodeType); //el tipo

console.log(navegacion.children[1].nodeType); //el tipo
console.log(navegacion.children[1].nodeType);




const card = document.querySelector('.card');

console.log(card.children[1].children[1].textContent);
card.children[1].children[1].textContent = 'alo';

card.children[0].src = 'img/hacer3.jpg';


// del hijo al padre

console.log(card.parentNode); // cuenta los espacios en blanco
console.log(card.parentElement.parentElement.parentElement);

// entre pares

console.log(card.nextElementSibling.nextElementSibling);


const ultimoCard = document.querySelector('.card:nth-child(4)');
console.log(ultimoCard.previousElementSibling);