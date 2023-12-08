from abc import abstractmethod
from store import Store
"""
f'Price per unit: {self.price}, Required amount: {quantity},'
                  f' Total purchase price: {self.price * quantity}'
"""


class Product:
    def __init__(self, name: str, price: int, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def deactivate(self):
        self.active = False

    def activate(self):
        self.active = True

    def is_active(self) -> bool:
        if self.quantity <= 0:
            self.deactivate()
        return self.active

    def get_quantity(self):
        return int(self.quantity)

    def set_quantity(self, quantity: int):
        try:
            self.quantity += quantity
            if self.quantity <= 0:
                self.deactivate()
            else:
                self.activate()
            print(f"Added {quantity} units to total amount of {self.quantity}")
        except TypeError:
            print(f"Wrong input, Please enter Integer")

    def show(self):
        print(f'{self.name}, Price: {self.price}, Quantity: {self.quantity}')

    def buy(self, quantity):
        inventory = self.quantity
        try:
            if 0 < quantity <= inventory and inventory > 0:
                self.quantity -= quantity
                if self.quantity <= 0:
                    self.deactivate()
                return self.price * quantity
                        # print(f'unit price: {self.price}, required amount: {quantity}'
                        #                             f' total price: {self.price * quantity},'
                        #                             f' new inventory: {self.quantity}'))
            else:
                return 'Error, Unable to complete the purchase'
        except TypeError as e:
            print('Wrong input type, please enter int', e)


# bose = Product(name="Bose QuietComfort Earbuds", price=250, quantity=500)
# mac = Product(name="MacBook Air M2", price=1450, quantity=100)
#
# print(bose.buy(50))
# print(mac.buy(100))
# print(mac.is_active())
#
# bose.show()
# mac.show()
#
# bose.set_quantity(1000)
# bose.show()
# mac.show()

bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
mac = Product("MacBook Air M2", price=1450, quantity=100)

store = Store([bose, mac])

pixel = Product("Google Pixel 7", price=500, quantity=-5)
store.add_product(pixel)
store.get_total_quantity()
print(store.get_all_products())
