//1. Person Info
/*
function createPerson(firstName, lastName, age) {
    const person = {
      firstName: firstName,
      lastName: lastName,
      age: age,
    };
  
    return person;
}
*/

//2. City
/*
function Info(object) {
  const matrix = Object.entries(object);

  for (let currentArrayIndex = 0; currentArrayIndex < matrix.length; currentArrayIndex++) {
    let key = matrix[currentArrayIndex][0];
    let value = matrix[currentArrayIndex][1];

    console.log(`${key} -> ${value}`);
  }
}
*/

//4. Convert to Object
/*
function ConvertToObject(json){
  const object = JSON.parse(json);

  const matrix = Object.entries(object);

  for (let currentArray = 0; currentArray < matrix.length; currentArray++) {
    let key = matrix[currentArray][0];
    let value = matrix[currentArray][1];
    
    console.log(`${key}: ${value}`)
  }
}
*/

//5. Convert to JSON
/*
function ConvertToJSON(firstName, lastName, hairColor){
  const object = {
    name: firstName,
    lastName,
    hairColor
  };

  console.log(JSON.stringify(object));
}

ConvertToJSON('George', 'Jones',
'Brown')
*/

//6. Phone Book
/*
function PhoneBook(array){
  let phonebook = {};

  for (let currentLine of array) {
    let line = currentLine.split(" ");

    let name = line[0];
    let number = line[1];

    phonebook[name] = number;
  }

  for (let key in phonebook) {
    console.log(`${key} -> ${phonebook[key]}`);
  }
}
*/

//7. Meetings
/*
function Meetings(appointments) {
  const scheduledMeetings = {};

  for (const appointment of appointments) {
    const [day, person] = appointment.split(' ');
    
    if (scheduledMeetings[day]) {
      console.log(`Conflict on ${day}!`);
    } else {
      scheduledMeetings[day] = person;
      console.log(`Scheduled for ${day}`);
    }
  }

  for (const day in scheduledMeetings) {
    console.log(`${day} -> ${scheduledMeetings[day]}`);
  }
}
*/

//8. Address Book
/*
function storeAddresses(input) {
  const addressBook = {};

  for (const entry of input) {
    const [name, address] = entry.split(':');
    addressBook[name] = address;
  }

  const sortedNames = Object.keys(addressBook).sort();

  for (const name of sortedNames) {
    console.log(`${name} -> ${addressBook[name]}`);
  }
}
*/

//9. Cats
/*
function Cats(input) {
  class Cat {
    constructor(name, age) {
      this.name = name;
      this.age = age;
    }

    meow() {
      console.log(`${this.name}, age ${this.age} says Meow`);
    }
  }

  const cats = [];

  for (const item of input) {
    const [name, age] = item.split(' ');
    const cat = new Cat(name, parseInt(age, 10));
    cats.push(cat);
    cat.meow();
  }
}
*/

//10. Songs
/*
function processSongs(input) {

  class Song {
    constructor(typeList, name, time) {
      this.typeList = typeList;
      this.name = name;
      this.time = time;
    }
  
    static filterSongsByType(songs, typeList) {
      if (typeList === 'all') {
        return songs.map(song => song.name);
      }
  
      return songs
        .filter(song => song.typeList === typeList)
        .map(song => song.name);
    }
  }
  

  const numberOfSongs = Number(input[0]);
  const songs = [];

  for (let i = 1; i <= numberOfSongs; i++) {
    const [typeList, name, time] = input[i].split('_');
    songs.push(new Song(typeList, name, time));
  }

  const typeListToFilter = input[input.length - 1];
  const filteredSongs = Song.filterSongsByType(songs, typeListToFilter);

  console.log(filteredSongs.join('\n'));
}
*/