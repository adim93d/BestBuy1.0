
class Store:
    def __init__(self, product_list):
        self.list_of_products = product_list

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
            if item.is_active():
                counter += item.quantity
        print(f'Total of {counter} in the inventory')
        return counter




