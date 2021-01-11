<?php
// arreglos indexados y como recorrerlo

$colors = array('rojo', 'verde', 'azul');
var_dump($colors);
print_r($colors);
echo $colors[1];
$colors[1] = 'rosa';

for ($i = 0; $i < sizeof($colors); $i++) {
    echo "\nindex: $i color: {$colors[$i]}\n";
}


// arreglos asociativos

$persona = array('nombre' => 'Agustin', 'apellido' => 'Olano', 'edad' => '18');
print_r($persona);
echo $persona['nombre'];

foreach ($persona as $key => $value) {
    echo "\nClave: $key Valor: $value\n";
}

// arreglos multidimensionales
$battleship = array(
    'A' => array('Mar', 'Barco', 'Mar', 'Mar'),
    'B' => array('Mar', 'Mar', 'Mar', 'Mar'),
    'C' => array('Mar', 'Mar', 'Barco', 'Mar'),
    'D' => array('Mar', 'Mar', 'Mar', 'Mar')
);

print_r($battleship);
echo $battleship['A'][1];

foreach ($battleship as $key => $value) {
    for ($i = 0; $i < sizeof($value); $i++) {
        echo "\n{$battleship[$key][$i]}\n";
    }
}
