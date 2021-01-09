<?php
// arreglos indexados

$colors = array('rojo', 'verde', 'azul');
var_dump($colors);
print_r($colors);
echo $colors[1];
$colors[1] = 'rosa';

// arreglos asociativos

$persona = array('nombre' => 'Agustin', 'apellido' => 'Olano', 'edad' => '18');
print_r($persona);
echo $persona['nombre'];

// arreglos multidimensionales
$battleship = array(
    array('A' => '')
);
