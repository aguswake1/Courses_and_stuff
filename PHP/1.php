<?php
/*trigger_error('Error al escribir', E_USER_ERROR);*/
$user = 'username';
/* con comillas simples no toma las variables
el ejemplo de abajo, la concatenacion con punto esta mal utilizada
se usa con comillas simples, con comillas dobles podemos ingresar directo
las variables*/

echo "hola \n \"" . $user . mt_rand();

function userName()
{
    global $user;
    echo "$user \n";
}

userName();

/* constantes
const no puede almacenar ni variables ni funciones
define si pero no se usa en clases creo */
const PATH1 = 'cursoPHP/index.php
buenardo pa, full picado';

echo PATH1;

define("PATH2", "cursoPHP/index2.php \n");
echo PATH2;

//print_r(get_defined_constants(true));   devuelve un arreglo de todas las constantes

/* heredoc y nowdoc
echo <<<FRASE
"Con esfuerzo y perseverancia podras alcanzar tus metas" \n $user
'alo'
FRASE;

comillas doble, el uso de variable se llama interpolacion
*/

$god = <<<FRASE
"Con esfuerzo y perseverancia podras alcanzar tus metas" \n $user
'alo'
FRASE;

echo $god;

$ido = <<<'FRASE'
"Con esfuerzo y perseverancia podras alcanzar tus metas" \n $user
'alo'
FRASE;

echo $ido;

/* tipos de vars */

echo gettype($user);
$user = (int)$user;
// tambien podemos usar floatval($user) intval() boolval() strval()
echo var_dump($user);  // muestra el tipo y valor de la var

echo "\n usando interpolacion {$user}\n";

$skere = 'no me la container';
// tercer parametro es opcional, es para decir hasta donde
echo substr($skere, -9, -5);
/* buscando una aguja (needle) en un pajar (haystack), nos devuelve la posicion del inicio donde encuentra
el segundo parametro, dentro del primero, en el tercer parametro (opcional) podemos
indicarle desde donde buscar
*/
echo strpos('hola gato', 'gato');
echo strpos('hola gato', 'a', 4);

/* primer argumento: lo que deseamos eliminar
segundo argumento: lo que queremos poner en reemplazo
tercer argumento: de donde deseamos realizar el reemplazo
cuarto argumento(opcional): creamos una variable que almacene la cantidad de reemplazos hechos */
echo str_replace("a", "*", "agua", $cont);
echo $cont;

/* mostrar en pantalla como sformat */
echo sprintf(" \n El otro dia fui a %s y gaste %d", 'palermo', 1000);
