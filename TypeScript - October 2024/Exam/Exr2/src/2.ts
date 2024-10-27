type City = {
    name: string;
    population: number;
    treasury: number;
    taxRate: number;

    collectTaxes(): void;
    applyGrowth(percentage: number): void;
    applyRecession(percentage: number): void;
};


function cityTaxes(name: string, population: number, treasury: number): City{
    let object: City = {
        name: name,
        population: population,
        treasury: treasury,
        taxRate: 10,

        collectTaxes(){
            this.treasury += this.population * this.taxRate;
        },

        applyGrowth(percentage){
            this.population += Math.floor(this.population * (percentage / 100) );
        },

        applyRecession(percentage){
            this.treasury -= Math.floor(this.treasury * (percentage / 100) );
        }
    };

    
    return object;
}



// input -----------------------------------
const city1 = 
  cityTaxes('Tortuga',
  7000,
  15000);
console.log(city1);


const city2 =
  cityTaxes('Tortuga',
  7000,
  15000);
city2.collectTaxes();
console.log(city2.treasury);
city2.applyGrowth(5);
console.log(city2.population);
