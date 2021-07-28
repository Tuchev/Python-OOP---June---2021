from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def get_sound(self):
        pass


class Cat(Animal):
    sound = "meow"

    def get_sound(self):
        return self.sound


class Dog(Animal):
    sound = "woof-woof"

    def get_sound(self):
        return self.sound

class Chicken(Animal):
    sound = "cluck"

    def get_sound(self):
        return self.sound

def animal_sound(animals: list):
    for animal in animals:
        print(animal.get_sound())


animals = [Cat(), Dog(), Chicken()]
animal_sound(animals)

## добавете ново животно и рефакторирайте кода да работи без да се налага да се правят промени по него
## при добавяне на нови животни
# animals = [Animal('cat'), Animal('dog'), Animal('chicken')]
