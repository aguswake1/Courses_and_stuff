iniciarApp();

function iniciarApp() {
    console.log('iniciando app...');
    segundaFuncion();
}

function segundaFuncion() {
    console.log('desde segunda funcion');
    usuarioAutenticado('Agustin');
}

function usuarioAutenticado(usuario) {
    console.log('autenticando usuario');
    console.log(`Usuario autenticado exitosamente, bienvenido ${usuario}`);

}