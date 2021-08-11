from unittest import TestCase, main

from project.card.trap_card import TrapCard
from project.player.advanced import Advanced
from project.battle_field import BattleField
from project.player.beginner import Beginner


class TestBattlefield(TestCase):
    def test_fight_attacker_is_dead(self):
        attacker = Advanced("Test1")
        enemy = Advanced("Test2")
        attacker.health = 0
        with self.assertRaises(ValueError) as ex:
            BattleField.fight(attacker, enemy)
        self.assertEqual("Player is dead!", str(ex.exception))

    def test_fight_enemy_is_dead(self):
        attacker = Advanced("Test1")
        enemy = Advanced("Test2")
        enemy.health = 0
        with self.assertRaises(ValueError) as ex:
            BattleField.fight(attacker, enemy)
        self.assertEqual("Player is dead!", str(ex.exception))

    def test_player_health_is_increased_if_beginners(self):
        pass

    def test_player_health_is_increased(self):
        attacker = Advanced("Test1")
        enemy = Advanced("Test2")
        card = TrapCard("TrapTest")
        attacker.card_repository.add(card)
        enemy.card_repository.add(card)
        self.assertEqual(250, attacker.health)
        self.assertEqual(250, enemy.health)
        BattleField.fight(attacker, enemy)
        self.assertEqual(135, attacker.health)
        self.assertEqual(135, enemy.health)
        self.assertFalse(attacker.is_dead)
        self.assertFalse(enemy.is_dead)

    def test_enemy_dies_in_battle(self):
        attacker = Advanced("Test1")
        enemy = Beginner("Test2")
        card = TrapCard("TrapTest")
        card_2 = TrapCard("TrapTest2")
        attacker.card_repository.add(card)
        attacker.card_repository.add(card_2)
        enemy.card_repository.add(card)
        self.assertEqual(250, attacker.health)
        self.assertEqual(50, enemy.health)
        enemy.health += 175
        BattleField.fight(attacker, enemy)
        self.assertEqual(260, attacker.health)
        self.assertFalse(attacker.is_dead)
        self.assertTrue(enemy.is_dead)


if __name__ == '__main__':
    main()