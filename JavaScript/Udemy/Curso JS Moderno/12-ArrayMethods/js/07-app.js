const meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio'];
const meses2 = ['Agosto', 'Septiembre'];
const meses3 = ['Octubre', 'Noviembre', 'Diciembre'];


// une arreglos
const mesesResultado = meses.concat(meses2, meses3, 'hola');

//spread operator
const resultado2 = [...meses, ...meses2, ...meses3, 'hola', ...'hola'];