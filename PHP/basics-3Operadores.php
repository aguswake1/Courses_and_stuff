<?php
$result = ((18 === '18') || !(18 === 18)) or (18 > 10 xor 18 > 20) && (10 != '10');
echo var_dump($result);

/* usamos la igualacion de una variable con ampersand refiriendonos
a la direccion de memoria para que a lo largo de todo el programa se copie el valor*/

$b = 20;
$a = &$b;

echo $b, $a . " \n";

$b **= 2;

echo ++$b, --$a . " \n";  // aumenta/disminuye despues imprime
echo $b--, $a++;  // imprime despues aumenta/disminuye

// operador ternario | 1expresion bool? 2expresion:3expresion si 1 es true pasa 2, si es false pasa 3
$age = 20;
echo $age >= 18 ? "\npodes comprar birra" : "pedile a alguien";

// operador elvis. Si no es null podes usar la variable isset()
$age2 = null;
echo $age2 ?: "\npedile a alguien";

// operador fusion null. Si la variable tiene valor imprime el valor
$age3;
echo $age3 ?? "\npedile a alguien";
