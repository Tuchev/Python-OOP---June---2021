from unittest import TestCase, main

from project.player.advanced import Advanced
from project.player.player_repository import PlayerRepository


class TestPlayerRepository(TestCase):
    def test_init_player_set_attributes(self):
        r = PlayerRepository()
        self.assertEqual(0, len(r.players))
        self.assertEqual(0, r.count)

    def test_add_player(self):
        r = PlayerRepository()
        self.assertEqual(0, len(r.players))
        self.assertEqual(0, r.count)
        player = Advanced("Test")
        r.add(player)
        self.assertEqual(1, len(r.players))
        self.assertEqual(1, r.count)

    def test_add_existing_player_raises(self):
        r = PlayerRepository()
        self.assertEqual(0, len(r.players))
        self.assertEqual(0, r.count)
        player = Advanced("Test")
        r.add(player)
        self.assertEqual(1, len(r.players))
        self.assertEqual(1, r.count)
        with self.assertRaises(ValueError) as ex:
            r.add(player)
        self.assertEqual("Player Test already exists!", str(ex.exception))
        self.assertEqual(1, len(r.players))
        self.assertEqual(1, r.count)

    def test_remove_player(self):
        r = PlayerRepository()
        self.assertEqual(0, len(r.players))
        self.assertEqual(0, r.count)
        player = Advanced("Test")
        r.add(player)
        self.assertEqual(1, len(r.players))
        self.assertEqual(1, r.count)
        r.remove(player.username)
        self.assertEqual(0, len(r.players))
        self.assertEqual(0, r.count)

    def test_remove_player_with_empty_string_raises(self):
        r = PlayerRepository()
        self.assertEqual(0, len(r.players))
        self.assertEqual(0, r.count)
        player = Advanced("Test")
        r.add(player)
        self.assertEqual(1, len(r.players))
        self.assertEqual(1, r.count)
        with self.assertRaises(ValueError) as ex:
            r.remove("")
        self.assertEqual("Player cannot be an empty string!", str(ex.exception))
        self.assertEqual(1, len(r.players))
        self.assertEqual(1, r.count)

    def test_find(self):
        r = PlayerRepository()
        self.assertEqual(0, len(r.players))
        self.assertEqual(0, r.count)
        player = Advanced("Test")
        r.add(player)
        self.assertEqual(1, len(r.players))
        self.assertEqual(1, r.count)
        founded = r.find(player.username)
        self.assertEqual("Test", founded.username)
        self.assertEqual(player.health, founded.health)
        self.assertEqual(player, founded)


if __name__ == '__main__':
    main()