class Person{
    private name: string;
    private age: number;

    constructor(name: string, age: number){
        this.name = name;
        this.age = age;
    }

    
    public getPersonInfo(){
        return `${this.name} is ${this.age} years old.`;
    }
    
    public setNameAndAge(name: string, age: string) {
        this.name = name;
        this.age = parseInt(age);
    }
}

const input: string = "Kristiyqn 21";
let arrOfObjParts: string[] = input.split(" ");

let person1 = new Person(arrOfObjParts[0], parseInt(arrOfObjParts[1]));

console.log(person1.getPersonInfo());
