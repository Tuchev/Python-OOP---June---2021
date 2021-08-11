from unittest import TestCase, main
from project.factory.paint_factory import PaintFactory


class TestPaintFactory(TestCase):
    def setUp(self) -> None:
        self.paint_factory = PaintFactory("Test", 100)

    def test_init_all_attributes(self):
        self.assertEqual("Test", self.paint_factory.name)
        self.assertEqual(100, self.paint_factory.capacity)
        self.assertEqual({}, self.paint_factory.ingredients)
        self.assertEqual(["white", "yellow", "blue", "green", "red"], self.paint_factory.valid_ingredients)

    def test_add_ingredients_invalid_product_type_raises(self):
        with self.assertRaises(TypeError) as ex:
            self.paint_factory.add_ingredient("purple", 2)
        self.assertEqual("Ingredient of type purple not allowed in PaintFactory", str(ex.exception))

    def test_add_ingredients_with_no_space_in_capacity(self):
        with self.assertRaises(ValueError) as ex:
            self.paint_factory.add_ingredient("white", 101)
        self.assertEqual("Not enough space in factory", str(ex.exception))

    def test_add_ingredients(self):
        self.assertEqual({}, self.paint_factory.ingredients)
        self.paint_factory.add_ingredient("white", 2)
        self.assertEqual({"white": 2}, self.paint_factory.ingredients)

    def test_add_ingredients_with_existing_ingredient_increase(self):
        self.assertEqual({}, self.paint_factory.ingredients)
        self.paint_factory.add_ingredient("white", 2)
        self.assertEqual({"white": 2}, self.paint_factory.ingredients)
        self.paint_factory.add_ingredient("white", 2)
        self.assertEqual({"white": 4}, self.paint_factory.ingredients)

    def test_remove_ingredient_with_invalid_ingredient_raises(self):
        with self.assertRaises(KeyError) as ex:
            self.paint_factory.remove_ingredient("purple", 2)
        self.assertEqual("'No such ingredient in the factory'", str(ex.exception))

    def test_remove_ingredient_with_valid_ingredient_with_invalid_capacity_raises(self):
        self.paint_factory.add_ingredient("white", 2)
        self.assertEqual({"white": 2}, self.paint_factory.ingredients)
        with self.assertRaises(ValueError) as ex:
            self.paint_factory.remove_ingredient("white", 4)
        self.assertEqual("Ingredients quantity cannot be less than zero", str(ex.exception))

    def test_remove_ingredient(self):
        self.paint_factory.add_ingredient("white", 4)
        self.paint_factory.remove_ingredient("white", 2)
        self.assertEqual({"white": 2}, self.paint_factory.ingredients)

    def test_products_property(self):
        self.paint_factory.add_ingredient("white", 2)
        self.assertEqual({"white": 2}, self.paint_factory.products)


if __name__ == "__main__":
    main()