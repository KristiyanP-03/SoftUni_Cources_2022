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
function createObjectsFromTable(input) {
    const objects = [];
  
    for (const row of input) {
      const [town, latitudeStr, longitudeStr] = row.split(' | ');
      const latitude = parseFloat(latitudeStr).toFixed(2);
      const longitude = parseFloat(longitudeStr).toFixed(2);
  
      const obj = {
        town: town,
        latitude: latitude,
        longitude: longitude,
      };
  
      objects.push(obj);
    }
  
    return objects;
  }
  
  const input = [
    'Sofia | 42.696552 | 23.32601',
    'Beijing | 39.913818 | 116.363625',
  ];
  
  const output = createObjectsFromTable(input);
  
  for (const obj of output) {
    console.log(obj);
  }
  