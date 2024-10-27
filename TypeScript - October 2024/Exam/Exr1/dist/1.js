function PrintAndSum(start_numer, end_number) {
    let start = start_numer;
    let end = end_number;
    let array_of_number = [];
    let sum_of_arrays_numbers = 0;
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
