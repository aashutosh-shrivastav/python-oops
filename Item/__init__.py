import csv
class Item:
    # quantity:int = 0
    # price:int = 0
    pay_rate:float = 8.0
    all = []
    def __init__(self,name:str,price:float = 0,quantity:int = 0) :
        
        assert price > 0 , f"Price {price} is not greater than 0"
        assert quantity >= 0 , f"Quantity {quantity} is not greater than or equal to 0"
        
        self.name = name
        self.price = price
        self.quantity = quantity

        self.all.append(self)
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}','{self.price}','{self.quantity}')"
        
    def apply_discount(self) :
        self.price = self.price*self.pay_rate

    def calculate_total_price(self) -> float:
        '''get total price wrt quantity'''
        return self.price*self.quantity
    
    @classmethod
    def instantiate_from_csv(cls):
        with open('./data/items.csv','r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
            for item in items:
                cls.all.append(
                    Item(
                        name =str(item.get("name")),
                        price = float(item.get("price",0)),
                        quantity = int(item.get("quantity",0))
                        ))
