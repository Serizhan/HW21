from Exceptions import NotEnoughSpace, NotEnoughProduct


class BaseClass:
    def __init__(self, items: dict, capacity):
        self.__items = items
        self.__capacity = capacity

    def add(self, name, amount):
        if not self.get_free_space() < amount:
            if name in self.__items:
                self.__items[name] += amount
            else:
                self.__items[name] = amount
        else:
            raise NotEnoughSpace

    def remove(self, name, amount: int):
        if name in self.__items and self.__items[name] >= amount:
            self.__items[name] -= amount
        else:
            raise NotEnoughProduct
        if self.__items[name] == 0:
            self.__items.pop(name)

    def get_free_space(self):
        load_space = 0
        for item in self.__items:
            load_space += self.__items[item]
        return self.__capacity - load_space

    def get_items(self):
        return self.__items

    def get_unique_items_count(self):
        return len(self.__items)
