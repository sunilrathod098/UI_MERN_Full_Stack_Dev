// check it is a prime or not
var n = 5
var isPrime = true

for (var i = 2; i< n; i++) {
    if (n % i === 0) {
        isPrime = false
        break
    }
}
console.log(isPrime);

// it is another approach using Math.sqrt roots
for (var i = 2; i <= Math.sqrt(n); i++) {
    if (n % i === 0) {
        isPrime = false
        break
    }
}
console.log(isPrime);