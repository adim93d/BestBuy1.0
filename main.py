import products
import store


def main():
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250),
                    ]

    store1 = store.Store(product_list)
    products1 = store1.get_all_products()
    print(store1.get_total_quantity())
    print(store1.order([(product_list[0], 1), (product_list[1], 2)]))


if __name__ == '__main__':
    main()
