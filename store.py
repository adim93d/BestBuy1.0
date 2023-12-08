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

    def get_all_products(self):
        active_products = []
        for item in self.list_of_products:
            if item.is_active():
                active_products.append(item)
        return active_products

    @staticmethod
    def order(shopping_list) -> float:
        name = 0
        quantity = 1
        total_price_counter = 0
        for item in shopping_list:
            total_price_counter += item[name].buy(item[quantity])
        return total_price_counter



