//VERY EASY

// helloWorld() returns "hello"

function helloWorld() {
	return "hello";
}

// Code a function that returns the first value from its array parameter. Examples: firstValue([9, 7, 11]) returns 9

function firstValue(array){
	return array[0];
}


//EASY
//MEDIUM


//HARD

// Return the smallest number from the array
function smallest(array){
  var menor = array[0];
  for (let i = 0;  i < array.length ; i++) {
    if (menor > array[i]){
      menor = array[i];
    }
  }
  return menor;
}

console.log(smallest([5,8,5,9,2,14]));


// Returns the sum of the numbers that make up the parameter
function totalSum(number){
  var resultado = 0;

  for (let i = 1; i <= number; i++){
    resultado += i;
  }

  return resultado;
}

console.log(totalSum(2));


// Returns the difference between the biggest and the smallest number.
var smallest, biggest;
function differenceMinMax(array){
  smallest = array[0];
  biggest = array[0];

  for (let i = 0; i < array.length ; i++){
    if (array[i] > biggest){
      biggest = array[i];
    } else if  (array[i] < smallest) {
      smallest = array[i];
    }else {
      continue;
    }
  }

  return biggest - smallest;
}

console.log(differenceMinMax([10,25,30,80]));



//VERY HARD

function reverse(array){
	array.reverse();
	return array;
