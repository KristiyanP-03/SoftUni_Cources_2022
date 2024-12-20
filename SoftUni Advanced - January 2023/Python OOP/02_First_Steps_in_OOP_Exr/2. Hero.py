class Hero:

    def __init__(self, name, health):
        self.name = name
        self.health = health

    def defend(self, damage: int):
        self.health -= damage

        if self.health <= 0:
            self.health = 0
            return  f"{self.name} was defeated"


    def heal(self, healing_power: int):
        self.health += healing_power

hero = Hero("Peter", 100)
print(hero.defend(50))
hero.heal(50)
print(hero.defend(99))
print(hero.defend(1))
