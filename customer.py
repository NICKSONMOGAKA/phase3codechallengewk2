class Customer:
    def __init__(self, name):
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        if len(name) < 1 or len(name) > 15:
            raise ValueError("Name must be between 1 and 15 characters")
        self._name = name
        self._orders = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        if len(value) < 1 or len(value) > 15:
            raise ValueError("Name must be between 1 and 15 characters")
        self._name = value

    def orders(self):
        return self._orders

    def coffees(self):
        return list(set(order.coffee for order in self._orders))

    def create_order(self, coffee, price):
        if not isinstance(coffee):
            raise ValueError("Coffee must be an instance of Coffee")
        if not isinstance(price, float) or price < 1.0 or price > 10.0:
            raise ValueError("Price must be a float between 1.0 and 10.0")
        order = (self, coffee, price)
        self._orders.append(order)
        return order

    @classmethod
    def most_aficionado(cls, coffee):
        customers = [customer for customer in cls.all_customers() if coffee in customer.coffees()]
        if not customers:
            return None
        return max(customers, key=lambda customer: sum(order.price for order in customer.orders() if order.coffee == coffee))

    @classmethod
    def all_customers(cls):
        # implement a way to remember all Customer objects
        pass