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
/*
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
*/

//6. Password Validator
/*
function PasswordValidator(password) {
    let flagValid = true;
  
    if (password.length < 6 || password.length > 10) {
      console.log("Password must be between 6 and 10 characters");
      flagValid = false;
    }
  
    let countOfDigits = 0;
  
    for (let index = 0; index < password.length; index++) {
      if (!/[a-zA-Z0-9]/.test(password[index])) {
        console.log("Password must consist only of letters and digits");
        flagValid = false;
        break;
      }
  
      if (/[0-9]/.test(password[index])) {
        countOfDigits += 1;
      }
    }
  
    if (countOfDigits < 2) {
      console.log("Password must have at least 2 digits");
      flagValid = false;
    }
  
    if (flagValid === true) {
      console.log("Password is valid");
    }
  }
  */

//7. NxN Matrix
/*
function Matrix(number){
    let line = "";
    for (let index = 0; index < number; index++) {
        line +=  number + " "; 
    }
    for (let index = 0; index < number; index++) {
            console.log(line);   
        }
}
*/

//8. Perfect Number
/*
function PerfectNumber(number) {
    if (number <= 0) {    
      return console.log("It's not so perfect.");
    }
  
    let sum = 0;
  
    for (let i = 1; i <= number / 2; i++) {
      if (number % i === 0) {
        sum += i;
      }
    }
  
    if (sum === number) {
      return console.log("We have a perfect number!");
    } else {
      return console.log("It's not so perfect.");
    }
}
*/

//9. Loading Bar
/*
function LoadingBar(number){
    if(number === 100)
    {
        return console.log("100% Complete!");
    }
    else {
        const loaded = number / 10;

        let bar = "";
        for (let index = 0; index < loaded; index++) {
            bar += "%";
        }
        
        for (let index = 0; index < (10 - loaded); index++) {
            bar += ".";
        }

        console.log(`${number}% [${bar}]`)
        console.log("Still loading...")
    }
}
*/

//10. Factorial Division
/*
function FactorialDivision(a, b){
    let sumOfA = 1;
    let sumOfB = 1;

    for (let index = 1; index <= a; index++) {
        sumOfA *= index;
    }

    for (let index = 1; index <= b; index++) {
        sumOfB *= index;
    }

    console.log(`${(sumOfA / sumOfB).toFixed(2)}`)
}
*/