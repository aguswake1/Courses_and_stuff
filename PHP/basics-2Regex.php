<?php
// PCRE expresion regular/regex --> \ # ~
$text = 'Hola mundo en 123';
$regex = "/Hola/";  // patron de busqueda

/* si la funcion encuentra coincidencias devuelve 1
por el contrario devuelve 0 */
echo preg_match($regex, $text);  // case sensitive function

// los metacaracteres tienen un papel importante en las expresiones regulares
$text = ' Hola mundo en 123';
$regex = "/^Hola/";  // el sombrerito hace que busque coincidencia al principio de la cadena

echo preg_match($regex, $text);  // devuelve 0

$text = 'mundo en 123 Hola';
$regex = "/Hola$/";  // el signo peso hace que busque coincidencia al final de la cadena

echo preg_match($regex, $text); // devuelve 1


$text = 'mundo en 123 hola';
/* modificadores despues del metacaracter, la i de insensitive hace que no distinga
entre mayusc y min. Hay otros que se pueden agregar, no los veremos ahora*/
$regex = "/Hola$/i";

echo preg_match($regex, $text); // devuelve 1

// metacaracteres agrupadores

$text = 'mundo en 123 hzla';
/* para que sea true uno de estos caracteres en el corchete tiene
que aparecer en la palabra */
$regex = "/H[aizo]la$/i";

echo preg_match($regex, $text); // devuelve 1
$text = 'mundo en 123 hbla';
/* para que sea true uno de los caracteres que comprende la secuencia
tiene que coincidir. Incluso se pueden utilizar numeros */
$regex = "/H[a-c]la$/i";

echo preg_match($regex, $text); // devuelve 1

$text = 'vivo en Mexico';
/* para que sea true debe contener x o j */
$regex = "/Me(x|j)ico$/i";

echo preg_match($regex, $text); // devuelve 1

// Secuencias de escape

$text = 'Los numeros son 1 4 5 6';
$regex = "/Me(x|j)ico$/i";

echo preg_match_all($regex, $text);
