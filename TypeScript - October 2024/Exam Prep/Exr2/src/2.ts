function LPC(input: string[]) {
    let CitiesProductsPricesMap: {
        [product: string]: {
            city: string,
            price: number
        }
    } = {};


    for (const line of input) {
        let [city, current_product_name, priceStr] = line.split(" | ");

        let priceNum = Number(priceStr);

        if (!CitiesProductsPricesMap[current_product_name] 
            || 
            CitiesProductsPricesMap[current_product_name].price > priceNum) {

            CitiesProductsPricesMap[current_product_name] = {
                city: city,
                price: priceNum
            };
            
        }

    }

    for (let product in CitiesProductsPricesMap) {
        const { city, price } = CitiesProductsPricesMap[product];
        console.log(`${product} -> ${price} (${city})`);
    }
}



const input: string[] = [
    'Sample Town | Sample Product | 1000',
    'Sample Town | Orange | 2',
    'Sample Town | Peach | 1',
    'Sofia | Orange | 3',
    'Sofia | Peach | 2',
    'New York | Sample Product | 1000.1',
    'New York | Burger | 10'
];

LPC(input);