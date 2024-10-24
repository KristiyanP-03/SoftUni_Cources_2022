"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.Cloth = void 0;
class Cloth {
    color;
    size;
    type;
    constructor(color, size, type) {
        this.color = color;
        this.size = size;
        this.type = type;
    }
    toString() {
        return `Product: ${this.type} with size ${this.size}, color ${this.color}`;
    }
}
exports.Cloth = Cloth;
const shirt = new Cloth("red", 42, "Shirt");
console.log(shirt.toString());
