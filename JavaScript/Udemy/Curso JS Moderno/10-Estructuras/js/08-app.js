// buena practica de if usarlo en una funcion

const puntaje = 500;

function revisarPuntaje() {
    if (puntaje > 400) {
        console.log('excelente');
        return;
    }
    if (puntaje > 300) {
        console.log('buen puntaje... felicidades');
        return;
    }
}

revisarPuntaje();