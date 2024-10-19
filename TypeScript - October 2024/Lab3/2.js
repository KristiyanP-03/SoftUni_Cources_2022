var Person = /** @class */ (function () {
    function Person(name, age) {
        this.name = name;
        this.age = age;
    }
    Person.prototype.getPersonInfo = function () {
        return "".concat(this.name, " is ").concat(this.age, " years old.");
    };
    Person.prototype.setNameAndAge = function (name, age) {
        this.name = name;
        this.age = parseInt(age);
    };
    return Person;
}());
var input = "Kristiyqn 21";
var arrOfObjParts = input.split(" ");
var person1 = new Person(arrOfObjParts[0], parseInt(arrOfObjParts[1]));
console.log(person1.getPersonInfo());
