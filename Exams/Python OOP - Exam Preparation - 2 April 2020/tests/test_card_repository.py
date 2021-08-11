from unittest import TestCase, main

from project.card.card_repository import CardRepository
from project.card.magic_card import MagicCard


class TestCardRepository(TestCase):
    def test_init_player_set_attributes(self):
        r = CardRepository()
        self.assertEqual(0, len(r.cards))
        self.assertEqual(0, r.count)

    def test_add_player(self):
        r = CardRepository()
        self.assertEqual(0, len(r.cards))
        self.assertEqual(0, r.count)
        player = MagicCard("Test")
        r.add(player)
        self.assertEqual(1, len(r.cards))
        self.assertEqual(1, r.count)

    def test_add_existing_player_raises(self):
        r = CardRepository()
        self.assertEqual(0, len(r.cards))
        self.assertEqual(0, r.count)
        player = MagicCard("Test")
        r.add(player)
        self.assertEqual(1, len(r.cards))
        self.assertEqual(1, r.count)
        with self.assertRaises(ValueError) as ex:
            r.add(player)
        self.assertEqual("Card Test already exists!", str(ex.exception))
        self.assertEqual(1, len(r.cards))
        self.assertEqual(1, r.count)

    def test_remove_player(self):
        r = CardRepository()
        self.assertEqual(0, len(r.cards))
        self.assertEqual(0, r.count)
        card = MagicCard("Test")
        r.add(card)
        self.assertEqual(1, len(r.cards))
        self.assertEqual(1, r.count)
        r.remove(card.name)
        self.assertEqual(0, len(r.cards))
        self.assertEqual(0, r.count)

    def test_remove_player_with_empty_string_raises(self):
        r = CardRepository()
        self.assertEqual(0, len(r.cards))
        self.assertEqual(0, r.count)
        card = MagicCard("Test")
        r.add(card)
        self.assertEqual(1, len(r.cards))
        self.assertEqual(1, r.count)
        with self.assertRaises(ValueError) as ex:
            r.remove("")
        self.assertEqual("Card cannot be an empty string!", str(ex.exception))
        self.assertEqual(1, len(r.cards))
        self.assertEqual(1, r.count)

    def test_find(self):
        r = CardRepository()
        self.assertEqual(0, len(r.cards))
        self.assertEqual(0, r.count)
        card = MagicCard("Test")
        r.add(card)
        self.assertEqual(1, len(r.cards))
        self.assertEqual(1, r.count)
        founded = r.find(card.name)
        self.assertEqual("Test", founded.name)
        self.assertEqual(card.health_points, founded.health_points)
        self.assertEqual(card.damage_points, founded.damage_points)
        self.assertEqual(card, founded)


if __name__ == '__main__':
    main()