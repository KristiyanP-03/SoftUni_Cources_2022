function turnArrayItemsToObjects(array) {
    for (var index = 0; index < array.length; index++) {
        var obj = array[index];
        var town_name = obj.split(" <-> ")[0];
        var population_count = parseInt(obj.split(" <-> ")[1], 10);
        var town = {
            name: town_name,
            population: population_count,
        };
        console.log(town.name + " : " + town.population);
    }
}
var inputArrayCase = ['Sofia <-> 1200000', 'Montana <-> 20000',
    'New York <-> 10000000', 'Washington <-> 2345000', 'Las Vegas <-> 1000000'];
turnArrayItemsToObjects(inputArrayCase);
