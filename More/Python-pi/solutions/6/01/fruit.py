"""
Fruit class definition module
"""

POSSIBLE_ORIGINS = (
    'America',
    'Asia',
    'Europe',
    'Africa',
    'Australia'
)


class Fruit:
    """
    Represents a fruit
    """

    def __init__(self, name, color, origin):
        self.name = name
        self.color = color
        self.origin = origin

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if name.strip() == '':
            raise ValueError('The fruit name should not be empty!')
        self._name = name.strip()

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        if color.strip() == '':
            raise ValueError('The fruit color should not be empty!')
        self._color = color.strip()

    @property
    def origin(self):
        return self._origin

    @origin.setter
    def origin(self, origin):
        if origin not in POSSIBLE_ORIGINS:
            raise ValueError(f'The origin {origin} is invalid!')
        self._origin = origin

    def __str__(self):
        return f'Fruit, called {self._name} from {self._origin}'

    def __repr__(self):
        return f'Fruit(\'{self._name}\', \'{self._color}\', \'{self._origin}\')'
