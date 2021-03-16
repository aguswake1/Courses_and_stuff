// ejercicio fizz buzz
//multiplo de 3 fizz
// multiplo de 5 buzz
//multiplo de ambos fizzbuzz



for (let i = 1; i < 100; i++) {
    if (i % 3 === 0 && i % 5 === 0) {
        console.log(`${i} fizzbuzz`);
    } else if (i % 3 === 0) {
        console.log(`${i} fizz`);
    } else if (i % 5 === 0) {
        console.log(`${i} buzz`);

    }

}