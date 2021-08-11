from unittest import TestCase, main

from project.card.magic_card import MagicCard

DAMAGE_POINTS = 5
HEALTH_POINTS = 80


class TestMagicCard(TestCase):
    def test_empty_name_raises(self):
        with self.assertRaises(ValueError) as ex:
            a = MagicCard("")
        self.assertEqual("Card's name cannot be an empty string.", str(ex.exception))

    def test_name_is_set(self):
        a = MagicCard("Test")
        self.assertEqual("Test", a.name)

    def test_health_is_set(self):
        a = MagicCard("Test")
        self.assertEqual(HEALTH_POINTS, a.health_points)

    def test_set_health_negative_raises(self):
        a = MagicCard("Test")
        with self.assertRaises(ValueError) as ex:
            a.health_points = -10
        self.assertEqual("Card's HP cannot be less than zero.", str(ex.exception))

    def test_damage_is_set(self):
        a = MagicCard("Test")
        self.assertEqual(DAMAGE_POINTS, a.damage_points)

    def test_set_damage_negative_raises(self):
        a = MagicCard("Test")
        with self.assertRaises(ValueError) as ex:
            a.damage_points = -10
        self.assertEqual("Card's damage points cannot be less than zero.", str(ex.exception))


if __name__ == '__main__':
    main()