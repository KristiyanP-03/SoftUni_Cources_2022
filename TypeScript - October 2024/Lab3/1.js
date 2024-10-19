var Car = /** @class */ (function () {
    function Car() {
    }
    Car.prototype.getBrand = function () {
        return this.brand;
    };
    Car.prototype.setBrnad = function (brand) {
        this.brand = brand;
    };
    Car.prototype.getModel = function () {
        return this.model;
    };
    Car.prototype.setModel = function (model) {
        this.model = model;
    };
    Car.prototype.getHorsepower = function () {
        return this.horsepower;
    };
    Car.prototype.setHorsepower = function (horsepower) {
        this.horsepower = parseInt(horsepower);
    };
    return Car;
}());
;
var vehicle = new Car();
var input = "Mazda 323f 88";
var arrayOfObjectParts = input.split(" ");
vehicle.setBrnad(arrayOfObjectParts[0]);
vehicle.setModel(arrayOfObjectParts[1]);
vehicle.setHorsepower(arrayOfObjectParts[2]);
console.log("The car is: " + vehicle.getBrand() + " " + vehicle.getModel() + " - " + vehicle.getHorsepower() + " HP.");
