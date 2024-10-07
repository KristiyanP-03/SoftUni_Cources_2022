let input: string = "5, 10";

let arrayOfNums: number[] | undefined = input?.split(", ").map(i => parseFloat(i.trim()));

const element1 = arrayOfNums[0];
const element2 = arrayOfNums[1];
        
console.log(element1 + element2);

