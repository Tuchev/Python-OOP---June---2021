from unittest import TestCase, main
from project.vehicle import Vehicle


class TestVehicle(TestCase):
    def setUp(self) -> None:
        self.vehicle = Vehicle(60.5, 131)

    def test_init_create_all_attributes(self):
        self.assertEqual(60.5, self.vehicle.fuel)
        self.assertEqual(60.5, self.vehicle.capacity)
        self.assertEqual(131, self.vehicle.horse_power)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)

    def test_drive_with_enough_fuel(self):
        self.assertEqual(60.5, self.vehicle.fuel)
        self.vehicle.drive(40)
        self.assertEqual(10.5, self.vehicle.fuel)

    def test_drive_without_fuel_raises(self):
        self.assertEqual(60.5, self.vehicle.fuel)
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(80)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_refuel_with_enough_capacity(self):
        self.assertEqual(60.5, self.vehicle.fuel)
        self.vehicle.drive(40)
        self.vehicle.refuel(10)
        self.assertEqual(20.5, self.vehicle.fuel)

    def test_refuel_without_enough_capacity(self):
        self.assertEqual(60.5, self.vehicle.fuel)
        self.vehicle.drive(40)
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(60)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_str_method(self):
        expected_result = "The vehicle has 131 horse power with 60.5 fuel left and 1.25 fuel consumption"
        str_msg = self.vehicle.__str__()
        self.assertEqual(expected_result, str_msg)


if __name__ == '__main__':
    main()
