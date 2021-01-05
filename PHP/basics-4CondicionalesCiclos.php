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
for ($i=0; $i < ; $i++) {
    # code...
}
