class Order:
    def __init__(self, customer, coffee, price):
        if not isinstance(customer):
            raise ValueError("Customer must be an instance of Customer")
        if not isinstance(coffee):
            raise ValueError("Coffee must be an instance of Coffee")
        if not isinstance(price, float) or price < 1.0 or price > 10.0:
            raise ValueError("Price must be a float between 1.0 and 10.0")
        self._customer = customer
        self._coffee = coffee
        self._price = price

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee

    @property
    def price(self):
        return self._price