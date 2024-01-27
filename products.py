class Promotion:
    def __init__(self, name):
        self.name = name

    def apply_promotion(self, product, quantity):
        raise NotImplementedError("Subclasses must implement apply_promotion method")


class PercentDiscount(Promotion):
    def __init__(self, name, percent):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity):
        discounted_price = product.price * (1 - self.percent / 100)
        return discounted_price * quantity


class SecondHalfPrice(Promotion):
    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        full_price_items = quantity // 2
        half_price_items = quantity - full_price_items
        discounted_price = (full_price_items * product.price + half_price_items * (product.price / 2))
        return discounted_price


class ThirdOneFree(Promotion):
    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        full_price_items = quantity // 3 * 2
        free_items = quantity - full_price_items
        discounted_price = full_price_items * product.price
        return discounted_price


class InvalidProductDetails(Exception):
    pass


class Product:
    def __init__(self, name: str, price: int, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True
        self.promotion = None  # Default: No promotion

    def validate_product_details(self, name, price):
        if not name or price < 0:
            raise InvalidProductDetails("Invalid product details. Name cannot be empty, and price cannot be negative.")

    def deactivate(self):
        if self.quantity <= 0:
            print('No inventory, Deactivating product')
            self.active = False

    def activate(self):
        self.active = True

    def is_active(self) -> bool:
        return self.active

    def get_quantity(self):
        return int(self.quantity)

    def set_quantity(self, quantity: int):
        try:
            if self.promotion:
                # Adjust the quantity based on the promotion
                adjusted_quantity = quantity - abs(quantity)  # Adjusted quantity considering the promotion
                quantity_adjusted = int(self.promotion.apply_promotion(self, adjusted_quantity))
                new_quantity = self.quantity + quantity_adjusted
            else:
                new_quantity = self.quantity + quantity

            if new_quantity < 0:
                raise ValueError("Cannot set negative quantity.")

            if new_quantity <= 0:
                self.quantity = 0  # Set quantity to 0 if it becomes negative or zero
                self.deactivate()
            else:
                self.quantity = new_quantity  # Update quantity
                self.activate()

            print('Inventory updated')

        except TypeError:
            print(f"Wrong input, please enter an integer")

    def set_promotion(self, promotion):
        self.promotion = promotion

    def remove_promotion(self):
        self.promotion = None

    def apply_promotion(self, quantity):
        if self.promotion:
            discounted_price = self.promotion.apply_promotion(self, quantity)
            return discounted_price
        else:
            return self.price * quantity

    def show(self):
        promotion_info = f', Promotion: {self.promotion.name}' if self.promotion else ''
        return f'Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}{promotion_info}'

    def buy(self, quantity):
        inventory = self.quantity
        try:
            if 0 < quantity <= inventory and inventory > 0:
                self.quantity -= quantity
                if self.quantity <= 0:
                    self.deactivate()
                return self.apply_promotion(quantity)
            else:
                return 'Error, Unable to complete the purchase'
        except TypeError as e:
            print('Wrong input type, please enter int', e)


class NonStockedProduct(Product):
    def __init__(self, name: str, price: int):
        super().__init__(name, price, quantity=0)

    def show(self):
        promotion_info = f', Promotion: {self.promotion.name}' if self.promotion else ''
        return f'Name: {self.name}, Price: {self.price}, Quantity: Unlimited (Non-Stocked){promotion_info}'

    def is_active(self) -> bool:
        return True

    def set_quantity(self, quantity: int):
        pass

    def apply_promotion(self, quantity):
        if self.promotion:
            return self.promotion.apply_promotion(self, quantity)
        else:
            return self.price * quantity


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


