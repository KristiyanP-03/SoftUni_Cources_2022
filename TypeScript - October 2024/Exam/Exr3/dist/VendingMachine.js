"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.VendingMachine = void 0;
class VendingMachine {
    buttonCapacity;
    drinks;
    constructor(buttonCapacity) {
        this.buttonCapacity = buttonCapacity;
        this.drinks = [];
    }
    addDrink(drink) {
        if (this.drinks.length < this.buttonCapacity) {
            this.drinks.push(drink);
        }
        else {
            console.log("ERROR CODE: NMS (No More Space)!");
        }
    }
    removeDrink(name) {
        let index = this.drinks.findIndex(indexDrink => indexDrink.name === name);
        if (index !== -1) {
            this.drinks.splice(index, 1);
            return true;
        }
        return false;
    }
    getLongest() {
        if (this.drinks.length === 0) {
            return "ERROR CODE: NDITVM (No Drinks in the Vending Machine)!";
        }
        let withBiggestVolume = 0;
        let targetDrink = this.drinks[0];
        for (const object of this.drinks) {
            if (object.volume > withBiggestVolume) {
                withBiggestVolume = object.volume;
                targetDrink = object;
            }
        }
        return targetDrink.toString();
    }
    getCheapest() {
        if (this.drinks.length === 0) {
            return "ERROR CODE: NDITVM (No Drinks in the Vending Machine)!";
        }
        let cheapestDrinkPrice = 999999999999.99;
        let targetDrink = this.drinks[0];
        for (const drink of this.drinks) {
            if (drink.price < cheapestDrinkPrice) {
                cheapestDrinkPrice = drink.price;
                targetDrink = drink;
            }
        }
        return targetDrink.toString();
    }
    buyDrink(name) {
        if (this.drinks.length === 0) {
            return "ERROR CODE: NDITVM (No Drinks in the Vending Machine)!";
        }
        for (const object of this.drinks) {
            if (object.name === name) {
                return object.toString();
            }
        }
    }
    getCount() {
        //console.log(this.drinks.length); // Даденият input е vendingMachine.getCount и output: [Function: getCount]
        return this.drinks.length; // За да работи променям vendingMachine.getCount на vendingMachine.getCount()
    }
    report() {
        if (this.drinks.length === 0) {
            return "ERROR CODE: NDITVM (No Drinks in the Vending Machine)!";
        }
        let output = "Drinks available: \n";
        output += this.drinks.map(drink => drink.toString()).join("\n");
        return output;
    }
}
exports.VendingMachine = VendingMachine;
