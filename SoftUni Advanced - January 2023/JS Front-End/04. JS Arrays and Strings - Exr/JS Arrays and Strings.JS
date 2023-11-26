//1. Array Rotation
/*
function ArrayRotation(array, rotations){
    for (let index = 0; index < rotations; index++) {
        array.push(array.shift());
    }

    console.log(array.join(" "));
}

ArrayRotation([51, 47, 32, 61, 21], 2);
*/

//2. Print every N-th Element from an Array
/*
function NElem(array, step) {
    let resultArray = [];

    for (let index = 0; index < array.length; index += step) {
        resultArray.push(array[index]);
    }

    return resultArray;
}

NElem(['5', '20', '31', '4', '20'], 2);
*/

//3. List Of Names 
/*
function ListOfNames(arryaOfNames){

    arryaOfNames.sort((a,b) => {
        return a.localeCompare(b);
    });

    for (let index = 0; index < arryaOfNames.length; index++) {
        console.log(index + 1 + "." + arryaOfNames[index]);
    }
}
ListOfNames(["John", "Bob", "Christina", "Ema"]);
*/

//4. Sorting Numbers
/*
function sortAlternate(arr) {
    arr.sort((a, b) => a - b);
    const result = [];

    for (let i = 0; i < Math.floor(arr.length / 2); i++) {
        result.push(arr[i]);
        result.push(arr[arr.length - 1 - i]);
    }

    if (arr.length % 2 !== 0) {
        result.push(arr[Math.floor(arr.length / 2)]);
    }

    return result;
}
*/

//5. Reveal Words
/*
function revealWords(words, templates) {
    const wordsArray = words.split(', ');
    const templatesArray = templates.split(' ');


    const replacedArray = templatesArray.map(template => {
        if (template.includes('*')) {
            const word = wordsArray.find(w => w.length === template.length);
            return word || template;
        } else {
            return template;
        }
    });


    const result = replacedArray.join(' ');
    return result;
}
*/

//6. Modern Times of #(HashTag)
/*
function findSpecialWords(input) {
    const regex = /#[a-zA-Z]+/g;
    const matches = input.match(regex);

    const validSpecialWords = matches.filter(word => /^[a-zA-Z]+$/.test(word.slice(1)));


    validSpecialWords.forEach(word => {
        console.log(word.slice(1));
    });
}
*/

//7.String Substring
/*
function findWordInText(word, text) {
    const lowercaseWord = word.toLowerCase();
    const lowercaseText = text.toLowerCase();

    if (lowercaseText.includes(lowercaseWord)) {
        console.log(word);
    } else {
        console.log(`${word} not found!`);
    }
}
*/

//8. Pascal-Case Splitter
// function splitPascalCase(input) {
//     const words = input.match(/[A-Z][a-z]*/g);

//     console.log(words.join(', '));
// }
