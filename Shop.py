from BaseClass import BaseClass
from Exceptions import ManyProducts


class Shop(BaseClass):
    def __init__(self, items, capacity=20):
        super().__init__(items, capacity)

    def add(self, name, amount: int):
        if self.get_unique_items_count() >= 5:
            raise ManyProducts
        else:
            super().add(name, amount)
