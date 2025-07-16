// here we display all the prime number from 1 to 100 in javascript
var primeNumbers = [];

for (var i = 2; i <= 100; i++) {
    var isPrime = true;
    for (var j = 2; j <= Math.sqrt(i); j++) {
        if (i % j === 0) {
            isPrime = false;
            break;
        }
    }
    if (isPrime) {
        primeNumbers.push(i); // every iteration the i is push in empty array
        }
}
console.log(primeNumbers);
