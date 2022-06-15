# python opps practice project
from keyboard import Keyboard
from phone import Phone

phone = Phone("Phone",100,5);

keyboard = Keyboard("Keyboard",1000,5);

# print(item)
# print(type(item))
# print(item.calculate_total_price())
# print(Item.all)


# print(Phone.all)

phone.apply_increment(20)
print(phone.price)
phone.apply_discount()
print(phone.price)

keyboard.apply_discount()
print(keyboard.price)
keyboard.apply_increment(20)
print(keyboard.price)
