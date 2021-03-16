const formulario = document.querySelector('#formulario');
formulario.addEventListener('submit', enviarForm)

function enviarForm(e) {
    // evita que haga el action para poder hacer cosas como consultar una api
    e.preventDefault();
    console.log(e.target.action);
    console.log(e.target.method);
}