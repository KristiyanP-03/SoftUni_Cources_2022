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
