import csv
class Item:
    # quantity:int = 0
    # price:int = 0
    pay_rate:float = 8.0
    all = []
    def __init__(self,name:str,price:float = 0,quantity:int = 0) :
        
        assert price > 0 , f"Price {price} is not greater than 0"
        assert quantity >= 0 , f"Quantity {quantity} is not greater than or equal to 0"
        
        self.__name = name
        self.__price = price
        self.quantity = quantity

        self.all.append(self)

#Encapsulation

    @property
    def price(self):
        return self.__price

    def apply_discount(self) :
        self.__price = self.__price*self.pay_rate

    def apply_increment(self,percentage):
        self.__price = (1+percentage/100)*self.__price


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,val:str):
        if len(val) > 10:
            raise Exception("The name is too long!")
        else:
            self.__name = val
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}','{self.__price}','{self.quantity}')"
        


    def calculate_total_price(self) -> float:
        '''get total price wrt quantity'''
        return self.__price*self.quantity
    
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
    
    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num,int):
            return True
        else:
            return False
