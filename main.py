import products
import store


def menu_input():
    user_input = input("What would you like to do?\n"
                       """Store Menu
----------
1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit
----------""")


def dispatch_table(input, store):
    functions = {
        1: print(store.Store.get_all_products()),
        2: print(store.Store.get_total_quantity()),
        3: store.Store.order(),
        4: quit()
    }


def start(store):
    while True:
        dispatch_table(menu_input(), store)


def main():
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250),
                    ]

    store1 = store.Store(product_list)
    products1 = store1.get_all_products()
    print(store1.get_total_quantity())
    print(store1.order([(products1[0], 1), (products1[1], 2)]))


if __name__ == '__main__':
    main()
