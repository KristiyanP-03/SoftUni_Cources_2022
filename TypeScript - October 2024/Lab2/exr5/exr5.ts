type Town = {
    name: string;
    population: number;
};


function turnArrayItemsToObjects(array: string[]) {
    for (let index = 0; index < array.length; index++) {
        let obj = array[index];


        let town_name = obj.split(" <-> ")[0];
        let population_count = parseInt(obj.split(" <-> ")[1], 10);
        
        let town: Town = {
            name: town_name,
            population: population_count,
        };


        console.log(town.name + " : " + town.population);
    }
}

const inputArrayCase: string[] = ['Sofia <-> 1200000', 'Montana <-> 20000',
    'New York <-> 10000000', 'Washington <-> 2345000', 'Las Vegas <-> 1000000'];

turnArrayItemsToObjects(inputArrayCase);
