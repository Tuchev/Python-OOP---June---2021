from unittest import TestCase, main

from project.controller import Controller
from project.player.advanced import Advanced
from project.player.beginner import Beginner


class TestController(TestCase):
    def test_init_controller(self):
        c = Controller()
        self.assertEqual(0, len(c.player_repository.players))
        self.assertEqual(0, len(c.card_repository.cards))

    def test_add_player_success(self):
        c = Controller()
        res1 = c.add_player("Beginner", "testbeginner")
        res2 = c.add_player("Advanced", "testadvanced")
        self.assertEqual("Successfully added player of type Beginner with username: testbeginner", res1)
        self.assertEqual("Successfully added player of type Advanced with username: testadvanced", res2)

    def test_add_card_success(self):
        c = Controller()
        res1 = c.add_card("Magic", "testmagic")
        res2 = c.add_card("Trap", "testtrap")
        self.assertEqual("Successfully added card of type MagicCard with name: testmagic", res1)
        self.assertEqual("Successfully added card of type TrapCard with name: testtrap", res2)

    def test_add_player_card(self):
        c = Controller()
        c.add_player("Beginner", "testbeginner")
        c.add_card("Magic", "testmagic")
        result = c.add_player_card("testbeginner", "testmagic")
        self.assertEqual("Successfully added card: testmagic to user: testbeginner", result)

    def test_fight(self):
        attacker = Advanced("Test1")
        enemy = Beginner("Test2")
        c = Controller()
        c.player_repository.add(attacker)
        c.player_repository.add(enemy)
        result = c.fight("Test1", "Test2")
        self.assertEqual("Attack user health 250 - Enemy user health 90", result)

    def test_report(self):
        attacker = Advanced("Test1")
        enemy = Beginner("Test2")
        c = Controller()
        c.player_repository.add(attacker)
        c.player_repository.add(enemy)
        result = c.report()
        self.assertEqual("Username: Test1 - Health: 250 - Cards 0\nUsername: Test2 - Health: 50 - Cards 0\n", result)


if __name__ == '__main__':
    main()
