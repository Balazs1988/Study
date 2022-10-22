"""
FruitStore class definition module
"""

from fruit import Fruit


class FruitStore:
    """
    Represents the store of fruits
    """

    def __init__(self):
        self._fruits = []

    def add(self, fruit: Fruit) -> None:
        """
        Add a new fruit to the store
        :param fruit: a fruit object
        :return: None
        """
        try:
            _ = self.find_fruit_by_name(fruit.name)
        except ValueError:
            self._fruits.append(fruit)
        else:
            raise ValueError(f'The fruit {fruit.name} has been already exists!')

    def remove(self, fruit_name: str) -> None:
        """
        Remove a fruit by name
        :param fruit_name: name of the fruit
        :return: None
        """
        filtered_fruits = []
        for fruit in self._fruits:
            if fruit.name != fruit_name:
                filtered_fruits.append(fruit)
        self._fruits = filtered_fruits

    def find_fruit_by_name(self, fruit_name: str) -> Fruit:
        """
        Find a fruit object by name
        :param fruit_name: name of the fruit
        :return: a fruit object
        """
        for fruit in self._fruits:
            if fruit.name == fruit_name:
                return fruit
        raise ValueError(f'The fruit {fruit_name} does not exists!')

    def collect_fruits_by_origin(self, origin: str) -> list:
        """
        Collect fruits by origin
        :param origin: origin of the fruit
        :return: list of fruit object from the same origin
        """
        result = []
        for fruit in self._fruits:
            if fruit.origin == origin:
                result.append(fruit)
        return result
