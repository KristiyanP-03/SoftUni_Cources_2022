function PrintAndSum(start_numer: number, end_number: number){
    let start: number = start_numer;
    let end: number = end_number;

    let array_of_number: number[] = [];
    let sum_of_arrays_numbers: number = 0;


    for (let index = start; index <= end; index++) {
        array_of_number.push(index);
        sum_of_arrays_numbers += index;
    }


    console.log(array_of_number.join(" "));
    console.log(`Sum: ${sum_of_arrays_numbers}`);
}



// input -----------------------------------
PrintAndSum(5, 10);
console.log("\n");
PrintAndSum(0, 26);
console.log("\n");
PrintAndSum(50, 60);