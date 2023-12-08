
class Store:
    def __init__(self, product):
        self.list_of_products = [product]

    def add_product(self, product):
        self.list_of_products.append(product)

    def remove_product(self, product):
        if product in self.list_of_products:
            self.list_of_products.remove(product)
        else:
            print('Error, Product not found')

    def get_total_quantity(self) -> int:
        counter = 0
        for item in self.list_of_products:
            print(str(item))


