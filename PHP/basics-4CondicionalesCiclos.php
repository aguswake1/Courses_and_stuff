<?php

$edad = 18;

// llevaria llaves si contuviera mas de una linea de codigo
if ($edad >= 18)
    echo 'podes ver la peli';
else
    echo 'no podes ver la peli';

/* -------------------------------- */

$shirt = 'verde';

// opcion 1
switch ($shirt) {
    case 'rojo':
        echo 'remera roja';
        break;
    case 'verde':
        echo 'remera verde';
        break;
    default:
        echo 'no esta el color que buscabas';
        break;
}

// opcion 2
switch ($shirt):
    case 'rojo':
        echo 'remera roja';
        break;
    case 'verde':
        echo 'remera verde';
        break;
    default:
        echo 'no esta el color que buscabas';
        break;
endswitch;

/* -------------------------------- */
for ($i = 0; $i < 10; ++$i) {
    echo "viendo iteración numero $i\n";
}

$cont = 12;

while ($cont <= 25) {
    echo "zapato numero $cont\n";
    ++$cont;
}

do {
    echo "zapato numero $cont\n";
} while ($cont <= 25);

// arreglos y sus iteraciones

$animales = array('gato', 'perro', 'elefante');
$db = array('Nombre' => 'Agustin', 'Apellido' => 'Olano', 'Edad' => '18');

foreach ($animales as $animal) {
    echo $animal . "\n";
}


foreach ($db as $key => $value) {
    echo "datos del usuario: $key: $value\n";
}
