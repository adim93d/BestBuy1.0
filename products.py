class Product:
    def __init__(self, name: str, price: float, quantity: int, active: bool):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = active

    def is_active(self) -> bool:
        return self.active

    def deactivate(self):
        self.active = False

    def activate(self):
        self.active = True

    def get_quantity(self) -> float:
        return float(self.quantity)

    def set_quantity(self, quantity: int):
        try:
            self.quantity += quantity
            if self.quantity <= 0:
                self.deactivate()
            else:
                self.activate()
            return f"Added {quantity} units to total amount {self.quantity}"
        except TypeError:
            return f"Wrong input, Please enter Integer"

    def show(self) -> str:
        if self.quantity <= 0:
            self.deactivate()
        else:
            self.activate()
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, Active: {self.active}"

    def buy(self, quantity) -> float:
        if quantity > self.quantity:
            return f"insufficient item quantity, Only {self.quantity} units available."
        else:
            purchase_price = quantity * self.price
            self.quantity = self.quantity - quantity
            return f"Total item price: ${purchase_price}"

