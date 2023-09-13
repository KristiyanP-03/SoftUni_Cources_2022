//1. Ages
/*
function Ages(age){
    let output = NaN;

    if (0 <= age && age <= 2) {
        output = "baby";
    }
    else if (3 <= age && age <= 13) {
        output = "child";
    }
    else if (14 <= age && age <= 19) {
        output = "teenager";
    }
    else if (20 <= age && age <= 65) {
        output = "adult";
    }
    else if (66 <= age) {
        output = "elder";
    }
    else{
        output = "out of bounds";
    }

    console.log(output)
}
*/

//2. Vacation
/*
function Vacation(group_of_people, type_of_the_group, day_of_the_week){
    let price = 0;
    let discont = 1;

    switch (type_of_the_group) {

        case "Students":
            if (group_of_people >= 30) {
                discont = 0.85
            }

            if (day_of_the_week === "Friday") {
                let cost = 8.45;

                price = (group_of_people * cost) * discont;
            }
            else if (day_of_the_week === "Saturday") {
                let cost = 9.80;

                price = (group_of_people * cost) * discont;
            }
            else if (day_of_the_week === "Sunday") {
                let cost = 10.46;

                price = (group_of_people * cost) * discont;
            }
            
            break;


        case "Business":
            if (group_of_people >= 100) {
                group_of_people = group_of_people - 10
            }

            if (day_of_the_week === "Friday") {
                let cost = 10.90;

                price = (group_of_people * cost) * discont;
            }
            else if (day_of_the_week === "Saturday") {
                let cost = 15.60;

                price = (group_of_people * cost) * discont;
            }
            else if (day_of_the_week === "Sunday") {
                let cost = 16;

                price = (group_of_people * cost) * discont;
            }
            break;


        case "Regular":
            if (group_of_people >= 10 && group_of_people <= 20) {
                discont = 0.95
            }

            if (day_of_the_week === "Friday") {
                let cost = 15;

                price = (group_of_people * cost) * discont;
            }
            else if (day_of_the_week === "Saturday") {
                let cost = 20;

                price = (group_of_people * cost) * discont;
            }
            else if (day_of_the_week === "Sunday") {
                let cost = 22.50;

                price = (group_of_people * cost) * discont;
            }
            break;
    


        default:
            break;
    }


    console.log(`Total price: ${price.toFixed(2)}`);
    
} 
*/

//3. Leap Year
/*
function Leap_Year(year) {
  if ((year % 4 === 0 && year % 100 !== 0) || year % 400 === 0) {
    return "yes";
  } else {
    return "no";
  }
}
*/

//4. Print And Sum
/*
function Print_And_Sum(start, end){
    let sum = 0;
    let printable_array = [];

    for (let index = start; index <= end; index++) {
        sum = sum + index;
        printable_array.push(index)
    }

    console.log(printable_array.join(' '));
    console.log(`Sum: ${sum}`)
}
*/

//5. Multiplication Table
/*
function Multiplication_Table(number){
    for (let index = 1; index <= 10; index++) {
        console.log(`${number} X ${index} = ${number * index}`);
    }
}
*/

//6. Sum Digits
/*
function Sum_Digits(number) {
    let string = number.toString();
    let char_by_char_array = string.split('');
    let sum = 0;

    for (let index = 0; index < char_by_char_array.length; index++) {
        sum = sum + parseInt(char_by_char_array[index])
    }
    console.log(sum)
}
*/

//7. Chars to String
/*
function Chars_to_String(char1, char2, char3) {
    console.log(char1 + char2 + char3)
}
*/

//8. Reversed Chars
/*
function Reversed_Chars(char1, char2, char3) {
    console.log(char3 + ' ' + char2 + ' ' + char1)
}
*/

//9. Fruit
/*
function Fruit(fruit, weightInGrams, pricePerKilogram){
    const weightInKilograms = weightInGrams / 1000;

    const money = (weightInKilograms * pricePerKilogram).toFixed(2);

    console.log(`I need $${money} to buy ${weightInKilograms.toFixed(2)} kilograms ${fruit}.`);
}
*/

//10. Same Numbers
/*
function Same_Numbers(number){
    const numberString = number.toString();

    const firstDigit = Number(numberString[0]);
        let sumOfDigits = 0;
    
    for (let i = 0; i < numberString.length; i++) {
        const currentDigit = Number(numberString[i]);
    
        sumOfDigits += currentDigit;
    }
    
    const allDigitsSame = numberString.split('').every(digit => digit === numberString[0]);
    
    console.log(allDigitsSame);
    console.log(sumOfDigits);
}
*/

//11. Road Radar
/*
function Road_Radar(speed, area) {

    const speedLimits = {
        motorway: 130,
        interstate: 90,
        city: 50,
        residential: 20
    };

    if (!speedLimits.hasOwnProperty(area)) {
        console.log('Invalid area');
        return;
    }

    const speedLimit = speedLimits[area];
    const difference = speed - speedLimit;

    let status = '';

    if (difference <= 0) {
        status = `Driving ${speed} km/h in a ${speedLimit} zone`;
    } else if (difference <= 20) {
        status = `The speed is ${difference} km/h faster than the allowed speed of ${speedLimit} - speeding`;
    } else if (difference <= 40) {
        status = `The speed is ${difference} km/h faster than the allowed speed of ${speedLimit} - excessive speeding`;
    } else {
        status = `The speed is ${difference} km/h faster than the allowed speed of ${speedLimit} - reckless driving`;
    }

    console.log(status);
}
*/

//12. Cooking by Numbers
/*
function Cooking_by_Numbers(stringed_number, ...list_of_oprs) {
    let number = parseInt(stringed_number);

    for (let operation of list_of_oprs) {
        switch (operation) {
            case 'chop':
                number /= 2;
                break;
            case 'dice':
                number = Math.sqrt(number);
                break;
            case 'spice':
                number += 1;
                break;
            case 'bake':
                number *= 3;
                break;
            case 'fillet':
                number *= 0.8;
                break;
        }
        console.log(number);
    }
}
*/