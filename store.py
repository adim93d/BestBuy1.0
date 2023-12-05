

class Store:
    def __init__(self, product_list):
        self.product_list = product_list

    def add_product(self, product):
        self.product_list.append(product)

    def remove_product(self, product):
        self.product_list.remove(product)

    def get_total_quantity(self) -> int:
        total_quantity = 0
        for item in self.product_list:
            total_quantity += item.quantity
        return total_quantity

    def get_all_products(self) -> []:
        active_products = []
        item_index = 1
        print()
        for item in self.product_list:
            if item.active:
                active_products.append(item.name)
                print(f"{item_index}. {item.name}, Price: ${item.price}, Quantity: {item.quantity}")
                item_index += 1
        print()
        return active_products

    def order(self, shopping_list):
        total_order_price = 0
        for item in shopping_list:
            total_order_price += item[1] * item[0].price
        print(f"Total shopping cart price: ${total_order_price}")
        return total_order_price
