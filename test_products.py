import pytest
import products

"""
Test that creating a normal product works.
Test that creating a product with invalid details (empty name, negative price) invokes an exception.
Test that when a product reaches 0 quantity, it becomes inactive.
Test that product purchase modifies the quantity and returns the right output.
Test that buying a larger quantity than exists invokes exception.
"""


def test_adding_product():
    assert products.Product("", price=1450, quantity=100)


def test_adding_product_negative_price():
    assert products.Product("MacBook Air M2", price=-10, quantity=100)


def test_no_inventory():
    item = products.Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    products.Product.buy(item, 500)
    assert item.active == False


def test_correct_quantity_after_purchase():
    item = products.Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    products.Product.buy(item, 200)
    assert item.quantity == 300


def test_purchase_bigger_than_inventory():
    item = products.Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    products.Product.buy(item, 700)
    assert item.quantity == 500

