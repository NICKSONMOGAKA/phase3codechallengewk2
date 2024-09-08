class Customer:
    all_customers = []

    def __init__(self, name):
        if not isinstance(name, str) or not (1 <= len(name) <= 15):
            raise ValueError("Name must be between 1 and 15 characters")
        self._name = name
        self._orders = []
        Customer.all_customers.append(self)

    @property
    def name(self):
        return self._name

    def orders(self):
        return self._orders

    def coffees(self):
        return list(set(order.coffee for order in self._orders))

    def create_order(self, coffee, price):
        if not isinstance(price, (int, float)) or not (1.0 <= price <= 10.0):
            raise ValueError("Price must be between 1.0 and 10.0")
        order = Order(self, coffee, price)
        self._orders.append(order)
        coffee.add_order(order)
        return order

    @classmethod
    def most_aficionado(cls, coffee):
        if not isinstance(coffee, Coffee):
            raise ValueError("Argument must be a Coffee instance")
        max_spent = 0
        aficionado = None
        for customer in cls.all_customers:
            total_spent = sum(order.price for order in customer.orders() if order.coffee == coffee)
            if total_spent > max_spent:
                max_spent = total_spent
                aficionado = customer
        return aficionado
