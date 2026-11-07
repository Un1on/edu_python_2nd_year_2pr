import csv

from main import OrderItem


def load_orders_from_csv(file_path: str) -> list[OrderItem]:
    """
    Loads orders from a csv file and converts them into a list of OrderItems
    :param file_path:
    :return:
    """
    orders = []
    with open(file_path, mode="r", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            customer = row.get("customer", "").strip()
            product_name = row.get("product_name", "").strip()

            if customer == "" or product_name == "":
                continue

            raw_price = row.get("price", "").strip()
            price = float(raw_price) if raw_price else 0.0

            raw_discount = row.get("discount", "").strip()
            discount = float(raw_discount) if raw_discount else 0.0

            raw_quantity = row.get("quantity", "1").strip()
            quantity = int(raw_quantity) if raw_quantity else 1

            item = OrderItem(customer, product_name, price, quantity, discount)
            orders.append(item)

    return orders


if __name__ == "__main__":
    items = load_orders_from_csv("sales.csv")
    print(f"Total order items: {len(items)}")

    for item in items:
        print(item)