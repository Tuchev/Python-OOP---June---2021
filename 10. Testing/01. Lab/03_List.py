class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)


from unittest import TestCase, main


class IntegerListTests(TestCase):
    def setUp(self) -> None:
        self.list_integer = IntegerList(5, 6, 7)

    def test_initialization_with_valid_numbers(self):
        self.assertEqual([5, 6, 7], self.list_integer._IntegerList__data)

    def test_initialization_with_invalid_numbers(self):
        list_integer = IntegerList(5.2, "6", 7.8)
        self.assertEqual([], list_integer._IntegerList__data)

    def test_add_integer_is_added(self):
        result = self.list_integer.add(100)
        self.assertEqual([5, 6, 7, 100], result)

    def test_add_non_integer_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.list_integer.add(5.5)
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_remove_index_return_element(self):
        el = self.list_integer.remove_index(0)
        self.assertEqual(5, el)
        self.assertEqual([6, 7], self.list_integer._IntegerList__data)

    def test_remove_index_not_in_range_raises(self):
        with self.assertRaises(IndexError) as ex:
            el = self.list_integer.remove_index(3)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_get_with_valid_index_return_element(self):
        el = self.list_integer.get(0)
        self.assertEqual(5, el)
        # self.assertEqual([5, 6, 7], self.list_integer._IntegerList__data)

    def test_get_with_not_valid_index_raises(self):
        with self.assertRaises(IndexError) as ex:
            el = self.list_integer.get(3)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert_add_element_at_index(self):
        self.list_integer.insert(0, 100)
        self.assertEqual([100, 5, 6, 7], self.list_integer._IntegerList__data)

    def test_insert_add_element_non_integer(self):
        with self.assertRaises(ValueError) as ex:
            self.list_integer.insert(0, "100")
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_insert_add_element_with_index_out_of_range_raises(self):
        with self.assertRaises(IndexError) as ex:
            self.list_integer.insert(3, 100)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_get_biggest(self):
        result = self.list_integer.get_biggest()
        self.assertEqual(7, result)

    def test_get_index(self):
        index = self.list_integer.get_index(5)
        self.assertEqual(0, index)


if __name__ == "__main__":
    main()
