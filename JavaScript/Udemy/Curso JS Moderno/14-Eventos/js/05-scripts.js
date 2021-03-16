// evento scroll
window.addEventListener('scroll', () => {
    // saber en pixeles cuanto nos desplazamos verticalmente
    const scrollPX = window.scrollY;
    console.log(scrollPX);
    const premium = document.querySelector('.premium');
    const ubicacion = premium.getBoundingClientRect();
    if (ubicacion.top < 784) {
        console.log('el elemento esta visible');
    }
})