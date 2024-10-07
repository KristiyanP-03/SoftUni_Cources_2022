var biggestNum = -99999999;
var arrOfNums = [5, -3, 16];
for (var index = 0; index < arrOfNums.length; index++) {
    var element = arrOfNums[index];
    if (element > biggestNum) {
        biggestNum = element;
    }
}
console.log(biggestNum);
