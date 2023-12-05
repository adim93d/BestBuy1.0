from abc import abstractmethod


class Product:
    def __init__(self, name: str, price: float, quantity: float):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def is_active(self) -> bool:
        return self.active

    def deactivate(self):
        self.active = False

    def activate(self):
        self.active = True

    @property
    def quantity(self) -> float:
        return self.quantity

    @quantity.setter
    def quantity(self, quantity: float):
        try:
            self.quantity += quantity
            if self.quantity <= 0:
                self.deactivate()
            else:
                self.activate()
            print(f"Added {quantity} units to total amount of {self.quantity}")
        except TypeError:
            print(f"Wrong input, Please enter Integer")



