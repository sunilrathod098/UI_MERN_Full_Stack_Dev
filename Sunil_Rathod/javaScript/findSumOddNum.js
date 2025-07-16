// find the sum of odd number in btw 990 to 201
var sum = 0
for (var i = 990; i >= 201; i--) {
    if (i % 2 !== 0) {
        sum += i
    }
}
console.log(sum)