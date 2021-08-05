from unittest import TestCase, main
from project.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self) -> None:
        self.mammal = Mammal("Test", "Test_type", "Test_sound")

    def test_init_create_all_attributes(self):
        self.assertEqual("Test", self.mammal.name)
        self.assertEqual("Test_type", self.mammal.type)
        self.assertEqual("Test_sound", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_make_sound(self):
        result = self.mammal.make_sound()
        self.assertEqual("Test makes Test_sound", result)

    def test_get_kingdom(self):
        result = self.mammal.get_kingdom()
        self.assertEqual("animals", result)

    def test_info(self):
        result = self.mammal.info()
        self.assertEqual("Test is of type Test_type", result)


if __name__ == "__main__":
    main()
