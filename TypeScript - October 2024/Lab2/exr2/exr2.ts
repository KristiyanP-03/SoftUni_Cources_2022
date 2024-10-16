type Obj_Person = {
    first_name: string,
    last_name: string,
    age: number
};


const obj1: Obj_Person = {
    first_name: "Pesho",
    last_name: "Pan",
    age: 15
};


function printObject(obj: Obj_Person) {
    console.log("firstName: " + obj.first_name);
    console.log("lastName: " + obj.last_name);
    console.log("age: " + obj.age);
};

printObject(obj1);