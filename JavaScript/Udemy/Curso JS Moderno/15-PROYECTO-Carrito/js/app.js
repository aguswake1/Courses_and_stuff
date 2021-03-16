/* por algun motivo, no funciona el listener cuando seleccionar la clase especifica,
capaz porque esta adentro del card, entonces usamos la tecnica del event blubbling
const agregarCarrito = document.querySelector('.agregar-carrito'); */
const contenedorCarrito = document.querySelector('#lista-carrito tbody');
const vaciarCarrito = document.querySelector('#vaciar-carrito');
const listaCursos = document.querySelector('#lista-cursos')
const carrito = document.querySelector('#carrito');

let articulosCarrito = [];

cargarEventListeners();

function cargarEventListeners() {
    // se almacenan datos cuando se hace click en 'agregar al carrito'
    listaCursos.addEventListener('click', e => {
        e.preventDefault();
        if (e.target.classList.contains('agregar-carrito')) {

            const cursoSeleccionado = e.target.parentElement.parentElement;


            let leerDatos = curso => {
                const datos = {
                    imagen: curso.querySelector('img').src,
                    nombre: curso.querySelector('h4').textContent,
                    precio: curso.querySelector('.precio span').textContent,
                    id: curso.querySelector('a').getAttribute('data-id'),
                    cantidad: 1
                    //id: e.target.getAttribute('data-id')
                }
                // destructuring
                const {
                    id
                } = datos;

                //revisa si un elemento ya existe en el carrito
                const existe = articulosCarrito.some(curso => curso.id === id);
                if (existe) {
                    // actualizamos la cantidad
                    const cursos = articulosCarrito.map(curso => {
                        if (curso.id === id) {
                            curso.cantidad += 1;
                            return curso;
                        } else {
                            return curso;
                        }
                    })
                    articulosCarrito = [...cursos];
                } else {
                    // agregar elementos al articulo
                    //articulosCarrito.push(datos);
                    articulosCarrito = [...articulosCarrito, datos];
                }
                carritoHTML();
            }
            leerDatos(cursoSeleccionado);
        }
    })
    // eliminar elementos
    carrito.addEventListener('click', e => {
        if (e.target.classList.contains('borrar-curso')) {
            let cursoId = e.target.getAttribute('data-id');
            // eliminar con filter por data id
            articulosCarrito = articulosCarrito.filter(curso => curso.id !== cursoId);
            //llamamos a la funcion para que haga efecto visualmente
            carritoHTML();
        }
    })

    vaciarCarrito.addEventListener('click', e => {
        articulosCarrito = [];
        carritoHTML();
    })
}


//muestra el carrito de compras en el html
function carritoHTML() {
    //sobrescribir carrito
    /* forma lenta
    contenedorCarrito.innerHTML = ''; */
    while (contenedorCarrito.firstChild) {
        contenedorCarrito.removeChild(contenedorCarrito.firstChild);
    }

    articulosCarrito.forEach(curso => {
        //destructuring
        const {
            imagen,
            nombre,
            precio,
            id,
            cantidad
        } = curso;

        const row = document.createElement('tr');
        row.innerHTML = `
        <td>
            <img src="${imagen}" width='100'>
        </td>
        <td>
            ${nombre}
        </td>
        <td>
            ${precio}
        </td>
        <td>
            ${cantidad}
        </td>
        <td>
            <a href="#" class="borrar-curso" data-id="${id}"> X </a>
        </td>`;

        //agrega el html
        contenedorCarrito.appendChild(row);
    })
}