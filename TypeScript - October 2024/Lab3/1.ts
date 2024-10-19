class Car{
    public brand: string;
    public model: string;
    public horsepower: number;

    public getBrand() {
        return this.brand;
    }
    public setBrnad(brand: string){
        this.brand = brand;
    }
    public getModel() {
        return this.model;
    }
    public setModel(model: string){
        this.model = model;
    }
    public getHorsepower() {
        return this.horsepower;
    }
    public setHorsepower(horsepower: string){
        this.horsepower = parseInt(horsepower);
    }
};

let vehicle = new Car();

const input: string = "Mazda 323f 88";
let arrayOfObjectParts: string[] = input.split(" ");

vehicle.setBrnad(arrayOfObjectParts[0]);
vehicle.setModel(arrayOfObjectParts[1]);
vehicle.setHorsepower(arrayOfObjectParts[2]);

console.log("The car is: " + vehicle.getBrand() + " " + vehicle.getModel() + " - " + vehicle.getHorsepower() + " HP.");