class Animal:
    def __init__(self, species):
        self.species = species

    def get_species(self):
        return self.species


class Cat(Animal):
    def __init__(self, species):
        super().__init__(species)

    def make_sound(self):
        return "meow"

class Dog(Animal):
    def __init__(self, species):
        super().__init__(species)

    def make_sound(self):
        return "wouf"

class Cow(Animal):
    def __init__(self, species):
        super().__init__(species)

    def make_sound(self):
        return "muu"


animals = [Cat('cat'), Dog('dog'), Cow('cow')]
for animal in animals:
    print(f"{animal.species} syas {animal.make_sound()}")




## добавете ново животно и рефакторирайте кода да работи без да се налага да се правят промени по него
## при добавяне на нови животни
# animals = [Animal('cat'), Animal('dog'), Animal('chicken')]
