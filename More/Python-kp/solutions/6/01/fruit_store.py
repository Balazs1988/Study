def add_fruit(name, color, origin):
    has_this_fruit = False
    for fruit in FruitStore.fruits_list:
        if fruit.name == name:
            has_this_fruit = True
    if not has_this_fruit:
        act_fruit = Fruit(name, color, origin)
        FruitStore.fruits_list.append(act_fruit)


def remove_fruit(name):
    for fruit in FruitStore.fruits_list:
        if fruit.name == name:
            FruitStore.fruits_list.remove(fruit)


def print_fruits_list():
    fruits_final_list = []
    for fruit in FruitStore.fruits_list:
        fruits_final_list.append(vars(fruit))
    return fruits_final_list


def fruits_by_name():
    fruits_final_list = []
    for fruit in FruitStore.fruits_list:
        fruits_final_list.append(vars(fruit))
    f_list = []
    for i in fruits_final_list:
        f_list.append(i['name'])
        f_list.sort()
    print(f_list)


def fruits_by_origin():
    fruits_final_list = []
    for fruit in FruitStore.fruits_list:
        fruits_final_list.append(vars(fruit))
    f_list = []
    for i in fruits_final_list:
        f_list.append(i['origin'])
        f_list.sort()
    print(f_list)


class Fruit:
    origin_list = ["Hungary", "Honduras", "Spain"]

    def __init__(self, name, color, origin):
        self.name = name
        self.color = color
        self.check_origin(origin)
        self.origin = origin

    def check_origin(self, origin):
        if origin not in self.origin_list:
            raise ValueError('Unknown origin!')


class FruitStore(Fruit):
    fruits_list = []

    def __init__(self):
        super().__init__(self.name, self.color, self.origin)


add_fruit('apple', 'red', 'Hungary')
add_fruit('pear', 'yellow', 'Hungary')

print(print_fruits_list())
remove_fruit('pear')
print(print_fruits_list())
add_fruit('pear', 'yellow', 'Hungary')
add_fruit('banana', 'yellow', 'Honduras')
add_fruit('orange', 'orange', 'Spain')
print(print_fruits_list())
fruits_by_name()
fruits_by_origin()
