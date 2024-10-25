import { Cloth } from "./Cloth";

export class Magazine{
    private type: string;
    private capacity: number;
    private clothes: Cloth[] = [];

    constructor(type: string, capacity: number){
        this.type = type;
        this.capacity = capacity;
    }


    addCloth(cloth: Cloth): void{
        if(this.clothes.length < this.capacity){
            this.clothes.push(cloth);
        }
    }

    removeCloth(color: string): boolean {
        const index = this.clothes.findIndex(cloth => cloth.color === color);
        
        if (index !== -1) {
            this.clothes.splice(index, 1);
            return true;
        }

        return false; 
    }
    
    getSmallestCloth(): Cloth {
        if (this.clothes.length === 0) {
            return {} as Cloth;
        }


        let smallestSize: number = 9999999999999;
        let smallestCloth: Cloth = this.clothes[0];

        for (const object of this.clothes) {
            if (object.size < smallestSize) {
                smallestSize = object.size;
                smallestCloth = object;
            }
        }

        return smallestCloth;
    }

    getCloth(color: string): Cloth{
        if (this.clothes.length === 0) {
            return {} as Cloth;
        }

        for (const object of this.clothes) {
            if (object.color === color) {
                return object
            }
        }

        return {} as Cloth;
    }

    getClothCount(): number{
        return this.clothes.length;
    }

    report(): string {
        // Sort clothes by size in ascending order
        const sortedClothes = this.clothes.sort((a, b) => a.size - b.size);
        
        // Map each cloth to its string representation and join them with a space
        const clothDescriptions = sortedClothes.map(cloth => cloth.toString()).join(" ");
        
        // Format the final output
        return `${this.type} magazine contains: \n${clothDescriptions}`;
    }
    
}

