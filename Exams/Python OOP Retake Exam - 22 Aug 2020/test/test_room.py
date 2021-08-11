from unittest import TestCase, main

from project.people.child import Child
from project.appliances.fridge import Fridge
from project.rooms.room import Room


class TestRoom(TestCase):
    def setUp(self) -> None:
        self.room = Room("Test", 100, 4)

    def test_init_all_attributes(self):
        self.assertEqual("Test", self.room.family_name)
        self.assertEqual(100, self.room.budget)
        self.assertEqual(4, self.room.members_count)
        self.assertEqual([], self.room.children)
        self.assertEqual(0, self.room.expenses)

    def test_expenses_property_with_negative_value(self):
        with self.assertRaises(ValueError) as ex:
            self.room.expenses = -1
        self.assertEqual("Expenses cannot be negative", str(ex.exception))

    def test_expenses_property(self):
        self.room.expenses = 45
        self.assertEqual(45, self.room.expenses)

    def test_expenses_property_with_zero_value(self):
        self.room.expenses = 0
        self.assertEqual(0, self.room.expenses)

    def test_calculate_expenses_with_zero_consumers(self):
        self.room.calculate_expenses([])
        self.assertEqual(0, self.room.expenses)

    def test_calculate_expenses_with_one_consumer(self):
        consumer = [Fridge()]
        self.room.calculate_expenses(consumer)
        self.assertEqual(consumer[0].get_monthly_expense(), self.room.expenses)

    def test_calculate_expenses_with_two_consumers(self):
        appliances = [Fridge()]
        children = [Child(5, 1, 2, 3)]
        self.room.calculate_expenses(appliances, children)
        expected = appliances[0].get_monthly_expense() + children[0].get_monthly_expense()
        self.assertEqual(expected, self.room.expenses)


if __name__ == '__main__':
    main()
