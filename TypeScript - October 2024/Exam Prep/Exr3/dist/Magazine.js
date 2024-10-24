"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.Magazine = void 0;
class Magazine {
    type;
    capacity;
    clothes;
    // Initialize properties in the constructor
    constructor(type, capacity) {
        this.type = type;
        this.capacity = capacity;
        this.clothes = []; // Initialize the clothes array
    }
    // Method to add a cloth to the collection
    addCloth(cloth) {
        if (this.clothes.length < this.capacity) {
            this.clothes.push(cloth);
            return true;
        }
        return false; // No room for more clothes
    }
    // Method to remove a cloth by its color
    removeCloth(color) {
        const index = this.clothes.findIndex(cloth => cloth.color === color);
        if (index !== -1) {
            this.clothes.splice(index, 1); // Remove the cloth
            return true; // Successfully removed
        }
        return false; // Cloth not found
    }
    // Method to get the smallest cloth
    getSmallestCloth() {
        if (this.clothes.length === 0)
            return null; // No clothes to check
        return this.clothes.reduce((smallest, current) => current.size < smallest.size ? current : smallest);
    }
    // Method to get a cloth by its color
    getCloth(color) {
        return this.clothes.find(cloth => cloth.color === color); // Returns cloth or undefined
    }
    // Method to get the count of clothes
    getClothCount() {
        return this.clothes.length; // Return the number of clothes
    }
    // Method to report the contents of the magazine
    report() {
        const sortedClothes = this.clothes.sort((a, b) => a.size - b.size); // Sort by size
        const clothDescriptions = sortedClothes.map(cloth => cloth.toString()).join(" "); // Create string
        return `${this.type} magazine contains: ${clothDescriptions}`; // Return formatted string
    }
}
exports.Magazine = Magazine;
