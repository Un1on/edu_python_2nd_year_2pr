
import pytest

from main import OrderItem


# Previous tests

def test_order_item_total_cost():
    item = OrderItem("Vlad", "Apple", 10.0, 10, 10)

    assert item.get_total_cost_raw() == 100.0
    assert item.get_discount_amount() == 10.0
    assert item.get_total_cost() == 90.0


def test_order_item_total_cost_with_zeroes():
    item = OrderItem("Vlad", "Apple", 10.0, 0, 0)

    assert item.get_total_cost_raw() == 0.0


def test_order_item_params_value_error():
    with pytest.raises(ValueError):
        OrderItem("Vlad", "Apple", 10.0, -10, 0)


# New delivery tests

def test_delivery_free_over_2000():
    item = OrderItem("Vlad", "Laptop", 2000.0, 1)

    assert item.get_delivery_cost("Київ") == 0.0
    assert item.get_delivery_cost("Львів") == 0.0
    assert item.get_delivery_cost("Луганськ") == 0.0


def test_delivery_cost_kyiv_and_other():
    item = OrderItem("Vlad", "Book", 500.0, 1)

    assert item.get_delivery_cost("Київ") == 50.0
    assert item.get_delivery_cost("київ") == 50.0
    assert item.get_delivery_cost(" КИЇВ ") == 50.0

    assert item.get_delivery_cost("Луганськ") == 100.0
    assert item.get_delivery_cost("Севастополь") == 100.0
    assert item.get_delivery_cost("Львів") == 100.0


def test_grand_total_calculation():
    item = OrderItem("Vlad", "Book", 500.0, 2)

    assert item.get_grand_total("Київ") == 1050.0
    assert item.get_grand_total("Львів") == 1100.0

    item2 = OrderItem("Vlad", "Laptop", 2500.0, 1)

    assert item2.get_grand_total("Львів") == 2500.0
