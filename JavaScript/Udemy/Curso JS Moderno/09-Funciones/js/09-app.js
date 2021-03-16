const reproductor = {
    reproducir: function (id) {
        console.log(`Reproduciendo cancion con id ${id}`);
    },
    pausar: function () {
        console.log('pausando');
    },
    crearPlaylist: function (nombre) {
        console.log(`creando Playlist: ${nombre}`);
    },
    reproducirPlaylist: function (nombre) {
        console.log(`reproduciendo: ${nombre}`);
    }
}

reproductor.reproducir(30);
reproductor.pausar();

reproductor.borrarCancion = function (id) {
    console.log(`borrando cancion con id ${id}`);
}

reproductor.borrar(30);