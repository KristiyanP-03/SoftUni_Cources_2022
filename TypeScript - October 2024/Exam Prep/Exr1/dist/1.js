function Calculator(first_number, operator, second_number) {
    let result = 0;
    switch (operator) {
        case "+":
            result = first_number + second_number;
            break;
        case "-":
            result = first_number - second_number;
            break;
        case "*":
            result = first_number * second_number;
            break;
        case "/":
            result = first_number / second_number;
            break;
        default:
            console.log("Input Error!");
            break;
    }
    console.log(result.toFixed(2));
}
Calculator(5, "+", 10);
Calculator(25.5, "-", 3);
Calculator(9, "/", 2);
Calculator(7, "*", 5);
