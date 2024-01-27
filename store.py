import products


class Store:
    def __init__(self, product_list):
        self.list_of_products = product_list
        self.cart = []

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

    def get_all_products(self) -> []:
        active_products = []
        item_index = 1
        print()
        for item in self.list_of_products:
            if item.is_active():
                active_products.append(item)
                print(f"{item_index}. {item.show()}")
                item_index += 1
        return active_products

    def order2(self):
        while True:
            print("\nOrder Menu:")
            print("1. Add to Cart")
            print("2. Remove from Cart")
            print("3. View Cart")
            print("4. Checkout")
            print("5. Continue ordering")
            print("6. Quit to main menu")

            try:
                choice = int(input("Choose an action (1-6): "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            order_dispatch_table = {
                1: self.add_to_cart,
                2: self.remove_from_cart,
                3: self.view_cart,
                4: self.checkout,
                5: lambda: None,
                6: lambda: print("Thank you for shopping with us!\n")
            }

            if choice in order_dispatch_table:
                order_dispatch_table[choice]()
                if choice == 6:
                    break
            else:
                print("Invalid choice. Please choose a number between 1 and 6.")

    def add_to_cart(self):
        self.get_all_products()

        try:
            user_product_input = int(input("Choose a product index number: "))
        except ValueError:
            print("Wrong input type, please enter an integer.")
            return

        if not (1 <= user_product_input <= len(self.list_of_products)):
            print("Invalid product index. Please choose a valid index.")
            return

        product = self.list_of_products[user_product_input - 1]

        try:
            user_quantity_input = int(input("Choose a quantity to add: "))
        except ValueError:
            print("Wrong input type, please enter an integer.")
            return

        if not product.is_active():
            print("Product is not active. Cannot add to the cart.")
        elif isinstance(product, products.LimitedProduct) and user_quantity_input > product.max_quantity:
            print(f"Error: Quantity exceeds the maximum allowed ({product.max_quantity}).")
        else:
            try:
                item_price = product.apply_promotion(user_quantity_input)
                self.cart.append({"product": product, "quantity": user_quantity_input, "total_price": item_price})
                product.set_quantity(-user_quantity_input)
                print(f"{user_quantity_input} {product.name}(s) added to the cart.")
            except ValueError as e:
                print(f"Error: {e}")

    def remove_from_cart(self):
        self.view_cart()
        try:
            index = int(input("Choose an item index to remove from the cart: "))
        except ValueError:
            print("Wrong input type, please enter an integer.")
            return

        if 1 <= index <= len(self.cart):
            removed_item = self.cart.pop(index - 1)
            product = removed_item['product']
            product.set_quantity(removed_item['quantity'])
            print(f"{removed_item['quantity']} {product.name}(s) removed from the cart.")
        else:
            print("Invalid item index. Please choose a valid index.")

    def view_cart(self):
        print("\nShopping Cart:")
        total_items = 0
        total_quantity = 0
        total_price = 0

        for i, item in enumerate(self.cart, start=1):
            total_items += 1
            total_quantity += item['quantity']
            total_price += item['total_price']
            print(f"{i}. {item['product'].name} - Quantity: {item['quantity']} - Price: ${item['total_price']}")

        print(f"\nTotal Items in Cart: {total_items}")
        print(f"Total Quantity in Cart: {total_quantity}")
        print(f"Total Price of Cart: ${total_price}")

    def checkout(self):
        self.view_cart()
        print("\nCheckout:")

        total_purchase_price_before_promotion = sum(item['product'].price * item['quantity'] for item in self.cart)
        total_purchase_price_after_promotion = sum(item['total_price'] for item in self.cart)

        print(f"Total Purchase Price before promotion: ${total_purchase_price_before_promotion}")
        print(f"Total Purchase Price after promotion: ${total_purchase_price_after_promotion}")

        amount_saved = total_purchase_price_before_promotion - total_purchase_price_after_promotion
        print(f"Amount Saved: ${amount_saved}")

        for item in self.cart:
            product = item['product']
            if product.is_active():
                product.set_quantity(-item['quantity'])

        self.clean_up_cart()
        self.cart = []
        print("Thank you for your purchase!\n")

    def clean_up_cart(self):
        self.cart = [item for item in self.cart if item['product'].is_active()]
        for i, item in enumerate(self.cart, start=1):
            product = item['product']
            if hasattr(product, 'set_index'):
                product.set_index(i)
