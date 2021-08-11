from unittest import TestCase, main

from project.player.advanced import Advanced


class TestAdvanced(TestCase):
    def test_empty_name_raises(self):
        with self.assertRaises(ValueError) as ex:
            a = Advanced("")
        self.assertEqual("Player's username cannot be an empty string.", str(ex.exception))

    def test_name_is_set(self):
        a = Advanced("Test")
        self.assertEqual("Test", a.username)

    def test_health_is_set(self):
        a = Advanced("Test")
        self.assertEqual(250, a.health)

    def test_set_health_negative_raises(self):
        a = Advanced("Test")
        with self.assertRaises(ValueError) as ex:
            a.health = -10
        self.assertEqual("Player's health bonus cannot be less than zero.", str(ex.exception))

    def test_is_dead(self):
        a = Advanced("Test")
        self.assertEqual(250, a.health)
        self.assertFalse(a.is_dead)
        a.health = 0
        self.assertEqual(0, a.health)
        self.assertTrue(a.is_dead)

    def test_take_damage_with_negative_value_raises(self):
        a = Advanced("Test")
        self.assertEqual(250, a.health)
        with self.assertRaises(ValueError) as ex:
            a.take_damage(-50)
        self.assertEqual("Damage points cannot be less than zero.", str(ex.exception))

    def test_take_damage(self):
        a = Advanced("Test")
        self.assertEqual(250, a.health)
        a.take_damage(50)
        self.assertEqual(200, a.health)

    def test_take_damage_player_will_be_dead(self):
        a = Advanced("Test")
        self.assertEqual(250, a.health)
        with self.assertRaises(ValueError):
            a.take_damage(260)


if __name__ == '__main__':
    main()
