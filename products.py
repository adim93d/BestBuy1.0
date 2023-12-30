class InvalidProductDetails(Exception):
    pass


class Product:
    def __init__(self, name: str, price: int, quantity: int):
        try:
            self.validate_product_details(name, price)
        except InvalidProductDetails as e:
            print(f"Error: {e}")

        self.index = None
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def validate_product_details(self, name, price):
        if not name or price < 0:
            raise InvalidProductDetails("Invalid product details. Name cannot be empty, and price cannot be negative.")

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


class NonStockedProduct(Product):
    def __init__(self, name: str, price: int, quantity: str):
        super().__init__(name, price, quantity='Unlimited (Non-Stocked)')

    def show(self):
        return f'Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}'


class LimitedProduct(Product):
    def __init__(self, name: str, price: int, quantity: int, maximum: int):
        super().__init__(name, price, quantity)
        self.max_quantity = maximum

    def show(self):
        return f'Name: {self.name}, Price: {self.price}, Quantity: Limited to {self.max_quantity}'

    def set_quantity(self, quantity: int):
        if quantity > self.max_quantity:
            raise ValueError(f"Quantity exceeds the maximum allowed ({self.max_quantity}).")
        super().set_quantity(quantity)
