// 1. Multiply the Number by 2
/* 
function MultiplytheNumberbyTwo(num)
{
    result = num * 2
    console.log(result)
}

MultiplytheNumberbyTwo(2)
*/



// 2. Student Information
/*
function StudentInformation(student_name, student_age, student_grade)
{ 
    let string = `Name: ${student_name}, Age: ${student_age}, Grade: ${student_grade.toFixed(2)}`

    console.log(string)
}
*/



// 3. Excellent grade
/* 
function ExcellentGrade(grade){
    let answer = NaN;

    if (grade >= 5.50)
    {
        answer = "Excellent";
    }
    else
    {
        answer = "Not excellent";
    }

    console.log(answer)
} 
*/



// 4. Month Printer 
/*
function Month_Printer(month_in_number){
	let output = NaN;
	
	switch(month_in_number){
		case 1: output = "January"; break;
		case 2: output = "February"; break;
		case 3: output = "March"; break;
		case 4: output = "April"; break;
		case 5: output = "May"; break;
		case 6: output = "June"; break;
		case 7: output = "July"; break;
		case 8: output = "August"; break;
		case 9: output = "September"; break;
		case 10: output = "October"; break;
		case 11: output = "November"; break;
		case 12: output = "December"; break;
		default: output = "Error!";
	 }
	 
	 console.log(output)
	
}
*/



// 5. Math Operations
/*
function Math_Operations(num_1, num_2, operation){
    let result = NaN;

    if(operation === "+")
    {
        result = num_1 + num_2
    }
    else if(operation === "-")
    {
        result = num_1 - num_2
    }
    else if(operation === "*")
    {
        result = num_1 * num_2
    }
    else if(operation === "/")
    {
        result = num_1 / num_2
    }
    else if(operation === "%")
    {
        result = num_1 % num_2
    }
    else if(operation === "**")
    {
        result = num_1 ** num_2
    }

    console.log(result)
}
*/

// 6. Largest Number
/*
function Largest_Number(...numbers) {
    let largest_number = -Infinity;

    numbers.forEach((number) => {
        if (number > largest_number) {
            largest_number = number;
        }
    });

    console.log(`The largest number is ${largest_number}.`);
}
*/

// 7. Theatre Promotions
/*
function Theatre_Promotions(type_of_the_day, age) {
    let output = NaN;

    switch (type_of_the_day) {

        case "Weekday":
            if (0 <= age && age <= 18) {
                output = "12$";
            } else if (18 < age && age <= 64) {
                output = "18$";
            } else if (64 < age && age <= 122) {
                output = "12$";
            } else {
                output = "Error!";
            }
            break;



        case "Weekend":
            if (0 <= age && age <= 18) {
                output = "15$";
            } else if (18 < age && age <= 64) {
                output = "20$";
            } else if (64 < age && age <= 122) {
                output = "15$";
            } else {
                output = "Error!";
            }
            break;



        case "Holiday":
            if (0 <= age && age <= 18) {
                output = "5$";
            } else if (18 < age && age <= 64) {
                output = "12$";
            } else if (64 < age && age <= 122) {
                output = "10$";
            } else {
                output = "Error!";
            }
            break;



        default:
            output = "Error!";
            break;
    }

    console.log(output);
}
*/

// 8. Circle Area
/*
function Circle_Area(input){
    if(typeof(input) != "number"){
        console.log(`We can not calculate the circle area, because we receive a ${typeof(input)}.`)
    }
    else{
        let result = Math.PI * Math.pow(input, 2);

        console.log(result.toFixed(2))
    }
}
*/


//9. Numbers from 1 to 5
/*
function Numbers_from_1_to_5(){
    for (let index = 1; index <= 5; index++) {
        console.log(index);        
    }
}
*/

//10. Numbers from M to N
/*
function Numbers_from_M_to_N(m, n){
    for (let index = m; index >= n; index--) {
        console.log(index);
    }
}
*/

//11. Sum First and Last Array Elements
/*
function Sum_First_and_Last_Array_Elements(the_array){
    let first_element = the_array[0];
    let last_element = the_array[the_array.length - 1];

    let result = first_element + last_element;

    console.log(result)
}
*/

//12. Reverse an Array of Numbers
/*
function Reverse_an_Array_of_Numbers(n, the_array) {
    if (n > the_array.length) {
        n = the_array.length;
    }

    let output = [];
    
    for (let index = n - 1; index >= 0; index--) {
        output.push(the_array[index]);
    }

    console.log(output.join(" "));
}
*/

//13. Even and Odd Subtraction
/*
function Even_and_Odd_Subtraction(the_array) {
    let even_sum = 0;
    let odd_sum = 0;

    for (let index = 0; index < the_array.length; index++) {
        if (the_array[index] % 2 === 0) {
            even_sum += the_array[index];
        } else {
            odd_sum += the_array[index];
        }
    }

    let result = even_sum - odd_sum;

    console.log(result);
}
*/

//14. Substring
/*
function Substring(string, start_index, end_index) {
    const result = string.substring(start_index, start_index + end_index);

  console.log(result);
}
*/

//15. Censored Words
/*
function Censored_Words(text, word) {
    const pattern = new RegExp(word, 'g');
    
    const result = text.replace(pattern, '*'.repeat(word.length));
    
    return result;
}
*/

//16. Count String Occurrences
/*
function Count_String_Occurrences(text, word) {
    const lowerText = text.toLowerCase();
    const lowerWord = word.toLowerCase();
  
    const words = lowerText.split(' ');
  
    let count = 0;
  
    for (const w of words) {
      if (w === lowerWord) {
        count++;
      }
    }
  
    return count;
}
*/