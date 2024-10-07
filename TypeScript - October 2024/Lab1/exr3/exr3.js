var input = "5, 10";
var arrayOfNums = input === null || input === void 0 ? void 0 : input.split(", ").map(function (i) { return parseFloat(i.trim()); });
var element1 = arrayOfNums[0];
var element2 = arrayOfNums[1];
console.log(element1 + element2);
