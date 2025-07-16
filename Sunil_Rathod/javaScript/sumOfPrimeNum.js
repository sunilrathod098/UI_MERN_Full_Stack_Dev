// this code is sum of all prime number
var sum = 0
for (var i = 200; i >= 20; i--) {
    if (i % 2 === 0) {
        sum += i
    }
}
console.log(sum)