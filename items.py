class Item:
    def __init__(self, price, weight, name):
        self.price = price
        self.weight = weight
        self.name = name


class Sword(Item):
    def __init__(self, damage):
        super().__init__(10, 5, "Sword")
        self.damage = damage