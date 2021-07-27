from project.lizard import Lizard
from project.mammal import Mammal


class Animal:
    def __init__(self, name):
        self.name = name


mammal = Mammal("Stella")
print(mammal.__class__.__bases__[0].__name__)
print(mammal.name)
lizard = Lizard("John")
print(lizard.__class__.__bases__[0].__name__)
print(lizard.name)
