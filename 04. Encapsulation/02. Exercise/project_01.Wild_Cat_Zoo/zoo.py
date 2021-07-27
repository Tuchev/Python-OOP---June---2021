from typing import List
from project.animal import Animal
from project.worker import Worker
from project.caretaker import Caretaker
from project.vet import Vet
from project.keeper import Keeper
from project.cheetah import Cheetah
from project.lion import Lion
from project.tiger import Tiger


class Zoo:
    name: str
    animals: List[Animal]
    workers: List[Worker]

    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def __has_capacity(self, attribute):
        attributes = {
            'animals': lambda: len(self.animals) < self.__animal_capacity,
            'workers': lambda: len(self.workers) < self.__workers_capacity,
        }

        return attributes[attribute]()

    @property
    def __has_animal_capacity(self):
        return self.__has_capacity('animals')

    @property
    def __has_workers_capacity(self):
        return self.__has_capacity('workers')

    def __has_enough_money(self, price):
        return self.__budget >= price

    def add_animal(self, animal, price):
        if not self.__has_enough_money(price):
            return f"Not enough budget"

        if isinstance(animal, Animal) \
                and self.__has_animal_capacity:
            self.__budget -= price
            self.animals.append(animal)
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        return f"Not enough space for animal"

    def hire_worker(self, worker):
        if isinstance(worker, Worker) \
                and self.__has_workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return f"Not enough space for worker"

    def fire_worker(self, worker_name):
        for idx, w_name in enumerate(self.workers):
            if w_name.name == worker_name:
                self.workers.pop(idx)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        for worker in self.workers:
            if self.__budget < worker.salary:
                return f"You have no budget to pay your workers. They are unhappy"
            self.__budget -= worker.salary
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        for animal in self.animals:
            if self.__budget < animal.money_for_care:
                return f"You have no budget to tend the animals. They are unhappy."
            self.__budget -= animal.money_for_care
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = []
        new_line = "\n"

        result.append(f"You have {len(self.animals)} animals")

        lions = [el for el in self.animals if isinstance(el, Lion)]
        if lions:
            result.append(f"----- {len(lions)} Lions:")
            for lion in lions:
                result.append(repr(lion))

        tigers = [el for el in self.animals if isinstance(el, Tiger)]
        if tigers:
            result.append(f"----- {len(tigers)} Tigers:")
            for tiger in tigers:
                result.append(repr(tiger))

        cheetahs = [el for el in self.animals if isinstance(el, Cheetah)]
        if cheetahs:
            result.append(f"----- {len(cheetahs)} Cheetahs:")
            for cheetah in cheetahs:
                result.append(repr(cheetah))

        return new_line.join(result)

    def workers_status(self):
        result = []
        new_line = "\n"

        result.append(f"You have {len(self.workers)} workers")

        keepers = [el for el in self.workers if isinstance(el, Keeper)]
        if keepers:
            result.append(f"----- {len(keepers)} Keepers:")
            for keeper in keepers:
                result.append(repr(keeper))

        caretakers = [el for el in self.workers if isinstance(el, Caretaker)]
        if caretakers:
            result.append(f"----- {len(caretakers)} Caretakers:")
            for caretaker in caretakers:
                result.append(repr(caretaker))

        vets = [el for el in self.workers if isinstance(el, Vet)]
        if vets:
            result.append(f"----- {len(vets)} Vets:")
            for vet in vets:
                result.append(repr(vet))

        return new_line.join(result)
