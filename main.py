import products
import store


def menu_input():
    user_input = input("\n"
                       """Store Menu
----------
1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit
----------\nWhat would you like to do: """)
    return user_input


def menu_dispatch_table(user_input, shop):
    functions_dispatcher = {1: list_products(shop),
                            4: quit}
    return functions_dispatcher[user_input]


def list_products(shop):
    shop.get_all_products()
    menu_dispatch_table(menu_input(), shop)


def start(shop):
    while True:
        menu_dispatch_table(menu_input(), shop)


def main():
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250),
                    ]

    best_buy = store.Store(product_list)
    start(best_buy)


if __name__ == '__main__':
    main()
