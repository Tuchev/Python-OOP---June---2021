from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCoupleWithChildren(Room):
    _COST = 30
    _PARENTS_COUNT = 2
    _APPLIANCES = [TV(), Fridge(), Laptop()]

    def __init__(self, family_name: str, salary_one: float, salary_two: float, *children):
        super().__init__(family_name, salary_one + salary_two, len(children) + YoungCoupleWithChildren._PARENTS_COUNT)
        self.room_cost = YoungCoupleWithChildren._COST
        self.children.extend(children)
        self.appliances = YoungCoupleWithChildren._APPLIANCES * self.members_count
        self.calculate_expenses(self.appliances, self.children)
