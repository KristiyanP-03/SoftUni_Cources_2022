"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.Magazine = void 0;
class Magazine {
    type;
    capacity;
    clothes = [];
    constructor(type, capacity) {
        this.type = type;
        this.capacity = capacity;
    }
    addCloth(cloth) {
        if (this.clothes.length < this.capacity) {
            this.clothes.push(cloth);
        }
    }
    removeCloth(color) {
        const index = this.clothes.findIndex(cloth => cloth.color === color);
        if (index !== -1) {
            this.clothes.splice(index, 1);
            return true;
        }
        return false;
    }
    getSmallestCloth() {
        if (this.clothes.length === 0) {
            return {};
        }
        let smallestSize = 9999999999999;
        let smallestCloth = this.clothes[0];
        for (const object of this.clothes) {
            if (object.size < smallestSize) {
                smallestSize = object.size;
                smallestCloth = object;
            }
        }
        return smallestCloth;
    }
    getCloth(color) {
        if (this.clothes.length === 0) {
            return {};
        }
        for (const object of this.clothes) {
            if (object.color === color) {
                return object;
            }
        }
        return {};
    }
    getClothCount() {
        return this.clothes.length;
    }
    report() {
        // Sort clothes by size in ascending order
        const sortedClothes = this.clothes.sort((a, b) => a.size - b.size);
        // Map each cloth to its string representation and join them with a space
        const clothDescriptions = sortedClothes.map(cloth => cloth.toString()).join(" ");
        // Format the final output
        return `${this.type} magazine contains: \n${clothDescriptions}`;
    }
}
exports.Magazine = Magazine;
