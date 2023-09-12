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