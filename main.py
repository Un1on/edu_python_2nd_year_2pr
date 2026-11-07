class OrderItem:
    """
    Order Item Class to represent a record of an order for given customer,
    price, quantity and discount in percent.
    """
    def __init__(self, customer: str, product_name: str, price: float, quantity: int, discount: float = 0.0):
        if price < 0 or quantity < 0 or discount < 0:
            raise ValueError("Please enter a valid price, quantity, discount")

        self.customer = customer
        self.product_name = product_name
        self.price = price
        self.quantity = quantity
        self.discount = discount

    def get_total_cost_raw(self) -> float:
        return self.price * self.quantity

    
    def get_delivery_cost(self, city: str = "Київ") -> float:
        # Free delivery for orders worth 2000 UAH or more
        if self.get_total_cost() >= 2000.0:
            return 0.0

        # Normalize city name: remove spaces and ignore case
        city = city.strip().lower()

        if city == "київ":
            return 50.0

        return 100.0

    def get_grand_total(self, city: str = "Київ") -> float:
        return self.get_total_cost() + self.get_delivery_cost(city)


    def get_discount_amount(self) -> float:
        return self.get_total_cost_raw() * (self.discount / 100)

    def get_total_cost(self) -> float:
        return self.get_total_cost_raw() - self.get_discount_amount()

    def to_dict(self) -> dict:
        return {
            "customer": self.customer,
            "product_name": self.product_name,
            "price": self.price,
            "quantity": self.quantity,
            "discount": self.discount,
            "total_cost_raw": self.get_total_cost_raw(),
            "discount_amount": self.get_discount_amount(),
            "total_cost": self.get_total_cost(),
        }

    def __str__(self) -> str:
        return (f"OrderItem(customer={self.customer}, product_name={self.product_name}, "
                f"price={self.price}, quantity={self.quantity}, discount={self.discount}) => "
                f"Total cost: {self.get_total_cost():.2f} UAH")


if __name__ == "__main__":
    item_apple = OrderItem("Vlad", "Apple", 10.0, 10)
    item_banana = OrderItem("Vlad", "Banana", 8.5, 5, 10.0)

    cart = [
        item_apple,
        item_banana
    ]

    total_cart = sum(
        item.get_total_cost() for item in cart
    )

    total_products = sum(
        item.quantity for item in cart
    )

    print(f"Total cart: {total_cart:.2f} UAH for {total_products}")