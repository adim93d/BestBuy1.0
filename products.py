class Product:
    def __init__(self, name: str, price: int, quantity: int):
        self.index = None
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def set_index(self, index):
        self.index = index

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
                print('No inventory, Deactivating product')
            else:
                self.activate()
                print('Inventory updated')
        except TypeError:
            print(f"Wrong input, Please enter Integer")

    def show(self):
        return f'Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}'

    def buy(self, quantity):
        inventory = self.quantity
        try:
            if 0 < quantity <= inventory and inventory > 0:
                self.quantity -= quantity
                if self.quantity <= 0:
                    self.deactivate()
                return self.price * quantity
            else:
                return 'Error, Unable to complete the purchase'
        except TypeError as e:
            print('Wrong input type, please enter int', e)
