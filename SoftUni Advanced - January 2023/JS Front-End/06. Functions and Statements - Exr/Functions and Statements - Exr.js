//1. Smallest of Three Numbers
/*
function SmallestOfThreeNumbers(...numbers) {
    let smallest_number = Math.min(...numbers);
    console.log(smallest_number);
}
*/

//2. Add and Subtract
/*
function AddAndSubtract(base, a, b){
    console.log((base + a) - b);
}
*/

//3. Characters in Range
/*
function CharactersInRange(char1, char2) {
    let output = "";

    const startCode = char1.charCodeAt(0);
    const endCode = char2.charCodeAt(0);

    const minCode = Math.min(startCode, endCode);
    const maxCode = Math.max(startCode, endCode);

    for (let index = minCode + 1; index < maxCode; index++) {
        output += " " + String.fromCharCode(index);
    }

    console.log(output);
}
*/

//4. Odd And Even Sum
/*
function OddAndEvenSum(number){
    const stringedNumber = number.toString();

    const digitArray = stringedNumber.split("").map(Number);

    let EvenSum = 0;
    let OddSum = 0;
   

    for (let index = 0; index < digitArray.length; index++) {
        if (digitArray[index] % 2 === 0) {
            EvenSum += digitArray[index]
        }
        else if(digitArray[index] % 2 != 0){
            OddSum += digitArray[index]
        }
        
    }

    console.log(`Odd sum = ${OddSum}, Even sum = ${EvenSum}`)
}
*/

//5. Palindrome Integers
function PalindromeIntegers(theArray) {
    let newElement;


    for (let index = 0; index < theArray.length; index++) {
        let element = theArray[index].toString();
        newElement = "";

        for (let elementI = element.length - 1; elementI >= 0; elementI--) {
            newElement += element[elementI];
        }

        if (element === newElement) {
            console.log("true");
        }
        else {
            console.log("false");
        }
    }
}

PalindromeIntegers([123,323,421,121])