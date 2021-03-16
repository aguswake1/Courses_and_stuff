const reproductor = {
    reproducir: id => console.log(`Reproduciendo cancion con id ${id}`),
    pausar: () => console.log('pausando'),
    crearPlaylist: nombre => console.log(`creando Playlist: ${nombre}`),
    reproducirPlaylist: nombre => console.log(`reproduciendo: ${nombre}`),
    set nuevaCancion(cancion) {
        this.cancion = cancion;
        console.log(`adding ${cancion}`);
    },
    get obteniendoCancion() {
        console.log(`${this.cancion}`);
    }
}
reproductor.nuevaCancion = 'ademas de mi remix';
reproductor.obteniendoCancion;
reproductor.reproducir(30);
reproductor.pausar();

reproductor.borrarCancion = id => console.log(`borrando cancion con id ${id}`);

reproductor.borrar(30);