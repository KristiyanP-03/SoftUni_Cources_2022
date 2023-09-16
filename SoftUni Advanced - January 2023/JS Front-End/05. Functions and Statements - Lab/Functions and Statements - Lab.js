//1. Format Grade
/*
function Format_Grade(grade) {
    let output;

    if (grade < 3.00) {
        output = "Fail (2)";
    } else if (grade >= 3.00 && grade < 3.50) {
        output = `Poor (${grade.toFixed(2)})`;
    } else if (grade >= 3.50 && grade < 4.50) {
        output = `Good (${grade.toFixed(2)})`;
    } else if (grade >= 4.50 && grade < 5.50) {
        output = `Very good (${grade.toFixed(2)})`;
    } else if (grade >= 5.50) {
        output = `Excellent (${grade.toFixed(2)})`;
    }

    console.log(output);
}

Format_Grade(4.33);
*/

//2. Math Power
/*
function Math_Power(number, power){
    console.log(number ** power)
}
*/

//3. Repeat String
/*
function Repeat_String(str, times_to_repeat) {
    return str.repeat(times_to_repeat);
}
*/

//4. Orders
/*
function Order(order, count){
let price = 0.00;

    switch (order) {

        case "coffee":
            price = 1.50;
            break;

        case "water":
            price = 1.00;
            break;

        case "coke":
            price = 1.40;
            break;
        
        case "snacks":
            price = 2.00;
            break;
    }

    total_price = price * count;
    
    console.log(`${total_price.toFixed(2)}`)
}
*/

//5. Simple Calculator  'multiply', 'divide', 'add' or 'subtract'
/*
function Simple_Calculator(numOne, numTwo, operator){
    if (operator === 'multiply') {
      console.log(numOne * numTwo);
    } else if (operator === 'divide') {
        console.log(numOne / numTwo);
    } else if (operator === 'add') {
        console.log(numOne + numTwo);
    } else if (operator === 'subtract') {
        console.log(numOne - numTwo);
    }
}
*/

//6. Sign Check
/*
function Sign_Check(numOne, numTwo, numThree) {
    const countNegatives = [numOne, numTwo, numThree].filter(num => num < 0).length;
  
    if (countNegatives % 2 === 0) {
      console.log("Positive");
    } else {
      console.log("Negative");
    }
}
*/