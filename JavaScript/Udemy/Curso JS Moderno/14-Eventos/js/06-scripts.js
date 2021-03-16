/*event bubbling se llama a la propagacion de un evento en varios
elementos debido a que estos se encuentran adentro de otro*/

const cardDiv = document.querySelector('.card');
const infoDiv = document.querySelector('.info');
const titulo = document.querySelector('.titulo');
// para que esto no suceda utilizamos el metodo stopPropagation

cardDiv.addEventListener('click', e => {
    e.stopPropagation();
    console.log('click en card');
})

infoDiv.addEventListener('click', e => {
    e.stopPropagation();
    console.log('click en info');
})

titulo.addEventListener('click', e => {
    e.stopPropagation();
    console.log('click en titulo');
})