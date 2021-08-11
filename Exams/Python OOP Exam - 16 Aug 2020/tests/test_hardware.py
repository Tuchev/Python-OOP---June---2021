from unittest import TestCase, main
from project.hardware.hardware import Hardware
from project.software.light_software import LightSoftware


class TestHardware(TestCase):
    def setUp(self) -> None:
        self.hardware = Hardware("Test", "Heavy", 500, 500)

    def test_init_all_attributes(self):
        self.assertEqual("Test", self.hardware.name)
        self.assertEqual("Heavy", self.hardware.type)
        self.assertEqual(500, self.hardware.capacity)
        self.assertEqual(500, self.hardware.memory)
        self.assertEqual([], self.hardware.software_components)

    def test_hardware_has_no_memory_software_is_installed_raises(self):
        software = LightSoftware("SoftName", 501, 501)
        with self.assertRaises(Exception) as ex:
            self.hardware.install(software)
        self.assertEqual("Software cannot be installed", str(ex.exception))

    def test_equal_capacity_and_memory_software_is_installed(self):
        software = LightSoftware("SoftName", 333, 1000)
        self.hardware.install(software)
        self.assertEqual(1, len(self.hardware.software_components))

    def test_software_is_installed(self):
        software = LightSoftware("SoftName", 200, 500)
        self.hardware.install(software)
        self.assertEqual(1, len(self.hardware.software_components))

    def test_uninstall_unexisting_software_does_not_complain(self):
        software = LightSoftware("SoftName", 200, 500)
        self.assertEqual(0, len(self.hardware.software_components))
        self.hardware.uninstall(software)
        self.assertEqual(0, len(self.hardware.software_components))

        #test data with some software
        software = LightSoftware("SoftName", 200, 500)
        self.hardware.install(software)
        self.assertIn(software, self.hardware.software_components)
        self.assertEqual(1, len(self.hardware.software_components))

        software_2 = LightSoftware("SoftName222", 200, 500)
        self.assertNotIn(software_2, self.hardware.software_components)
        self.assertEqual(1, len(self.hardware.software_components))
        self.hardware.uninstall(software_2)
        self.assertEqual(1, len(self.hardware.software_components))

    def test_uninstall_software(self):
        software = LightSoftware("SoftName", 200, 500)
        self.hardware.install(software)
        self.assertIn(software, self.hardware.software_components)
        self.assertEqual(1, len(self.hardware.software_components))

        self.hardware.uninstall(software)
        self.assertNotIn(software, self.hardware.software_components)
        self.assertEqual(0, len(self.hardware.software_components))



if __name__ == '__main__':
    main()
