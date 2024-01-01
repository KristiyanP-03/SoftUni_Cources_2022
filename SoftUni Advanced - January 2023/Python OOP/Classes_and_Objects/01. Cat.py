class Cat:      #taka se suzdava klass v Python
    def __init__(self, name, age, fur):            #state - registrirash harakteristikite
        self.name = name
        self.age = age
        self.fur = fur

    def say_meow(self):                               #behavior - povedenie
        return f"{self.name}: meow"


myCat = Cat("Misho", 2, "White")          #suzdavane na instanciq (nov object ot klasa)
print(myCat.say_meow())                                 #polzvane na metod
