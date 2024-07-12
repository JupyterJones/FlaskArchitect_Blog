
//1.
for (var i = 0; i <= 1000; i+=100) {
  console.log(i);
}

//2.
for (var i = 1; i <= 128; i*=2) {
  console.log(i);
}

//.3
for (var i = 0; i <= 10; i+=2) {
  console.log(i);
}

//.4
for (var i = 3; i <= 15; i+=3)
  console.log(i);


//5.
for ( var i = 9; i >= 0; i-=1) {
  console.log(i);
}

//6.
for ( var i = 1; i <= 4; i++) {
  for (g = 0; g < 3; g++)
      console.log(i);
}

//7.
for ( var g = 0; g < 3; g++) {
  for (i = 1; i <= 4; i++)
      console.log(i);
}

console.log("scope!");

// var globalVar = "Crystal!";
//
// var sum = function(x, y) {
//   // hiding variable inside function
//   var result = x +y;
//   return result;
// };
//
// sum(4, 6);
//
// console.log(result);
//
// global variable
// var hello = scoped("Bob");
// console.log(hello);

// var result1 = scoped("Bob");
// console.log(result);
// console.log(greeting);

// var keyword and scope

var greeting = "Hello!";

var scoped = function(name) {
  // hiding
  // local variable
  var greeting = "Hello" + name;
  return greeting;
};

// function arguments - optional

function multiply(num1, num2) {
  if (num2 === undefined) {
    num2 = 2;
  }
  var result = num1 * num2;
  return result;
}

var result1 = multiply(4,5)
console.log(result1);

var result2 = multiply(5);
console.log(result2)



