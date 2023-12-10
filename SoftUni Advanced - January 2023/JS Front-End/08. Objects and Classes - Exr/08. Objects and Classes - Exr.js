//1. Employees
/*
function Employees(array){
    for (let index = 0; index < array.length; index++) {
        const object = {
            employeeName: array[index],
            personalNum: array[index].length,
        };
        console.log(`Name: ${object.employeeName} -- Personal Number: ${object.personalNum}`);
    }
}

Employees([
    'Silas Butler',
    'Adnaan Buckley',
    'Juan Peterson',
    'Brendan Villarreal'
])
*/

//2. Towns
/*
function TownsInfo(array) {
    for (let index = 0; index < array.length; index++) {
      let currentTownsInfo = array[index].split(" | ");
  
      let townModel = {
        town: currentTownsInfo[0],
        latitude: Number(currentTownsInfo[1]).toFixed(2), 
        longitude: Number(currentTownsInfo[2]).toFixed(2)
      };
  
      console.log(townModel);
    }
}

TownsInfo(['Sofia | 42.696552 | 23.32601', 'Beijing | 39.913818 | 116.363625'] );
*/

//3. Store Provision
/*
function StoreProvision(stockArray, deliveryArray) {
    let resultArray = [];
    let stockObject = {};


    for (let i = 0; i < stockArray.length; i += 2) {
        let provisionName = stockArray[i];
        let quantity = Number(stockArray[i + 1]);
        stockObject[provisionName] = quantity;
    }


    for (let i = 0; i < deliveryArray.length; i += 2) {
        let provisionName = deliveryArray[i];
        let quantity = Number(deliveryArray[i + 1]);

        if (stockObject.hasOwnProperty(provisionName)) {
            stockObject[provisionName] += quantity;
        } else {
            stockObject[provisionName] = quantity;
        }
    }


    for (let key in stockObject) {
        resultArray.push({ provisionName: key, quantity: stockObject[key] });
    }
    for (let i = 0; i < resultArray.length; i++) {
        console.log(`${resultArray[i].provisionName} -> ${resultArray[i].quantity}`);
    }
}


StoreProvision(
    [
        'Chips', '5', 'CocaCola', '9', 'Bananas',
        '14', 'Pasta', '4', 'Beer', '2'
    ],
    [
        'Flour', '44', 'Oil', '12', 'Pasta', '7',
        'Tomatoes', '70', 'Bananas', '30'
    ]
);
*/

//4. Movies 
/*
function Movies(input) {
    const movies = [];
  
    for (const line of input) {
      const tokens = line.split(' ');
  
      if (tokens[0] === 'addMovie') {
        const movieName = tokens.slice(1).join(' ');
        movies.push({ name: movieName });
      } else {
        const movieIndex = movies.findIndex(movie => movie.name === tokens[0]);
  
        if (movieIndex !== -1) {
          if (tokens.includes('directedBy')) {
            const director = tokens.slice(tokens.indexOf('directedBy') + 1).join(' ');
            movies[movieIndex].director = director;
          } else if (tokens.includes('onDate')) {
            const date = tokens.slice(tokens.indexOf('onDate') + 1).join(' ');
            movies[movieIndex].date = date;
          }
        }
      }
    }
  
    for (const movie of movies) {
      if (movie.name && movie.director && movie.date) {
        console.log(JSON.stringify(movie));
      }
    }
  }
*/

//5. Inventory
/*
function createHeroRegister(input) {
    const heroes = [];
  
    for (const line of input) {
      const [heroName, heroLevel, itemsString] = line.split(' / ');
      const hero = {
        name: heroName,
        level: Number(heroLevel),
        items: itemsString ? itemsString.split(', ') : []
      };
      heroes.push(hero);
    }
  
    const sortedHeroes = heroes.sort((a, b) => a.level - b.level);
  
    for (const hero of sortedHeroes) {
      console.log(`Hero: ${hero.name}`);
      console.log(`level => ${hero.level}`)
      console.log(`items => ${hero.items.join(', ')}`)
    }
}
*/

//6. Word Tracker
/*
function wordsTracker(input) {
    const targetWords = input[0].split(' ');
    const wordOccurrences = {};
  
    for (let i = 1; i < input.length; i++) {
      const wordsInCurrentLine = input[i].toLowerCase().split(/\W+/);
  
      for (const word of wordsInCurrentLine) {
        if (targetWords.includes(word) && word !== '') {
          if (!wordOccurrences[word]) {
            wordOccurrences[word] = 1;
          } else {
            wordOccurrences[word]++;
          }
        }
      }
    }
  
    const sortedWords = Object.entries(wordOccurrences)
      .sort((a, b) => b[1] - a[1])
      .forEach(([word, count]) => console.log(`${word} - ${count}`));
  }
*/

//7. Odd Occurrences
/*
function oddOccurrences(input) {
    const words = input.toLowerCase().split(' ');
    const wordCount = {};
  
    for (const word of words) {
      if (wordCount[word]) {
        wordCount[word]++;
      } else {
        wordCount[word] = 1;
      }
    }
  
    const oddWords = Object.keys(wordCount).filter(word => wordCount[word] % 2 !== 0);
  
    console.log(oddWords.join(' '));
}
*/

//8. Piccolo
/*
function piccolo(input) {
    const parkingLot = {};
  
    for (const entry of input) {
      const [action, carNumber] = entry.split(', ');
  
      if (action === 'IN') {
        parkingLot[carNumber] = true;
      } else if (action === 'OUT') {
        delete parkingLot[carNumber];
      }
    }
  
    const parkedCars = Object.keys(parkingLot).sort();
  
    if (parkedCars.length > 0) {
      console.log(parkedCars.join('\n'));
    } else {
      console.log('Parking Lot is Empty');
    }
  }
*/

//9. Make a Dictionary
/*
function makeDictionary(input) {
    const dictionary = {};
  
    for (const jsonString of input) {
      const jsonObj = JSON.parse(jsonString);
      const [term, definition] = Object.entries(jsonObj)[0];
      dictionary[term] = definition;
    }
  
    const sortedTerms = Object.keys(dictionary).sort();
  
    for (const term of sortedTerms) {
      console.log(`Term: ${term} => Definition: ${dictionary[term]}`);
    }
 }
 */

 //10. Class Vehicle
 /*
 class Vehicle {
    constructor(type, model, parts, fuel) {
      this.type = type;
      this.model = model;
      this.parts = parts;
      this.fuel = fuel;
    }
  
    drive(fuelLoss) {
      this.fuel -= fuelLoss;
      this.parts.quality = this.parts.engine * this.parts.power;
    }
  }
  */