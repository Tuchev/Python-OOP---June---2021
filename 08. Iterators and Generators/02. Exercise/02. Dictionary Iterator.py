from typing import Any, Dict


class dictionary_iter:
    def __init__(self, el_dict: Dict[Any, Any]):
        self.el_dict = el_dict
        self.__el_dict = iter(self.el_dict.items())

    def __iter__(self):
        self.__el_dict = iter(self.el_dict.items())
        return self

    def __next__(self):
        val = next(self.__el_dict)
        return val


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
