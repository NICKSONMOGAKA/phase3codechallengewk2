class Customer:
    all_customers = []

    def _init_(self, name):
        self.name = name
        Customer.all_customers.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value
        else:
            raise ValueError("Name must be between 1 and 15 characters.")

    def orders(self):
        return [order for order in Order.all_orders if order.customer == self]

    def coffees(self):
        return list(set(order.coffee for order in self.orders()))

    def create_order(self, coffee, price):
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        customer_spending = {}
        for order in coffee.orders():
            if order.customer in customer_spending:
                customer_spending[order.customer] += order.price
            else:
                customer_spending[order.customer] = order.price
        return max(customer_spending, key=customer_spending.get, default=None)


class Coffee:
    all_coffees = []

    def _init_(self, name):
        self.name = name
        Coffee.all_coffees.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) >= 3:
            self._name = value
        else:
            raise ValueError("Coffee name must be  with at least 3 characters.")

    def orders(self):
        return [order for order in Order.all_orders if order.coffee == self]

    def customers(self):
        return list(set(order.customer for order in self.orders()))

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        total_price = sum(order.price for order in self.orders())
        return total_price / len(self.orders()) if self.orders() else 0


class Order:
    all_orders = []

    def _init_(self, customer, coffee, price):
        if not isinstance(customer, Customer):
            raise ValueError("Customer must be a Customer instance.")
        if not isinstance(coffee, Coffee):
            raise ValueError("Coffee must be a Coffee instance.")
        if not (1.0 <= price <= 10.0):
            raise ValueError("Price must be between 1.0 and 10.0.")
        
        self._customer = customer
        self._coffee = coffee
        self._price = price
        Order.all_orders.append(self)

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee

    @property
    def price(self):
        return self._price


def test_coffee_shop():
    Nick = Customer("Nick")
    bob = Customer("bob")
    tito = Customer("tito")

    espresso = Coffee("Espresso")
    latte = Coffee("Latte")

    order1 = Order(Nick, espresso, 4.0)
    order2 = Order(bob, espresso, 3.0)
    order3 = Order(tito, latte, 5.0)

    print(Nick.name)
    print(bob.orders())
    print(tito.coffees())
    
    print(espresso.orders())
    print(espresso.customers())
    print(espresso.num_orders())
    print(espresso.average_price())

    new_order = Nick.create_order(latte, 5.0)
    print(new_order.customer.name)
    print(new_order.coffee.name)
    print(new_order.price)

    print(Customer.most_aficionado(espresso).name)


test_coffee_shop()
