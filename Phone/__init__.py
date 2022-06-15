from item import Item

class Phone(Item):
    pay_rate: float = 0.5

    def __init__(self, name: str, price: float = 0, quantity: int = 0,broken_phone:int = 0):
        super().__init__(name, price, quantity)
        assert broken_phone >=0 , f"Broken Phones {broken_phone} cannot be smaller than 0"
        self.broken_phone = broken_phone