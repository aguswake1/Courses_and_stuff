<?php
function subjects($estudiante = 'Estudiante')
{
    return "$estudiante tus materias son: Matematica, Lengua, Biologia, Geografia, Civica e Historia\n";
}

echo subjects('Tobias');
echo subjects();

// igualar a direccion de memoria para escapar el scope

$number = 18;
$scape = 20;

function scope($num, &$numGlobal)
{
    return $num += 8 and $numGlobal -= 10;
}

scope($number, $scape);
echo $number, $scape;

// funcion recursiva

function incremento($num)
{
    if ($num < 20) {
        echo "\n$num\n";
        incremento(++$num);
    }
}

incremento(10);

// funcion, convertir multiples operaciones de array

function arreglos($num1, $num2)
{
    return array($num1 + $num2, $num1 - $num2, $num1 * $num2);
}

list($suma, $resta, $multiplicacion) = arreglos(10, 15);

echo "\nEl resultado de la suma es $suma, el de la resta es $resta, y la multiplicacion es $multiplicacion";

// funcion anonima
$anonim = function ($num1, $num2) {
    return $num1 + $num2;
};

echo $anonim(10, 20);

// funcion variable
function fVariable()
{
    echo "\n cambiando nombre";
}

$varia = 'fVariable';
$varia();

// Declaraciones de tipo escalar
declare(strict_types=1);  // esto en realidad va en al principio del documento
function validate(int $num): int  // se debe pasar un argumento int y retornar un int
{
    echo "\n $num";
    return 'hola';
}
