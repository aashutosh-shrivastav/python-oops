from item import Item

class Keyboard(Item):
    pay_rate: float = 0.7
    def __init__(self, name: str, price: float = 0, quantity: int = 0):
        super().__init__(name, price, quantity)
