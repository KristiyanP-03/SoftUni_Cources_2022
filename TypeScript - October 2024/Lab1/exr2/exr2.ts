let biggestNum: number = -99999999;

let arrOfNums: number[] = [5, -3, 16, 6];

for (let index = 0; index < arrOfNums.length; index++) {
    const element = arrOfNums[index];
    
    if (element > biggestNum) {
        biggestNum = element;
    }
}

console.log(biggestNum);

/*
let biggestNum: number = -99999999;

// Get user input and process it
let userInput: string | null = prompt("Please enter a list of numbers separated by commas:");

// Ensure input is not null and convert it into an array of numbers
if (userInput !== null) {
    let arrOfNums: number[] = userInput
        .split(",")                       // Split the input string by commas
        .map(item => parseFloat(item.trim()))  // Convert each string to a number
        .filter(item => !isNaN(item));         // Filter out invalid numbers
    
    // Loop through the array to find the biggest number
    for (let index = 0; index < arrOfNums.length; index++) {
        const element = arrOfNums[index];
        
        if (element > biggestNum) {
            biggestNum = element;
        }
    }

    console.log(`The biggest number is: ${biggestNum}`);
} else {
    console.log("No input provided.");
}
*/