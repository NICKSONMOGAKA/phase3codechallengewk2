Coffee Shop Management System
Overview
This is a simple coffee shop management system implemented in Python. The system consists of three main classes: Customer, Coffee, and Order. The system allows customers to place orders for different types of coffee, and it keeps track of the orders, customers, and coffee types.

Classes and Methods
Customer
The Customer class represents a customer in the system.
It has the following methods:
__init__: Initializes a new customer with a name.
name: Returns the customer's name.
orders: Returns a list of the customer's orders.
coffees: Returns a list of unique coffee types ordered by the customer.
create_order: Creates a new order for the customer.
most_aficionado: Returns the customer who has ordered the most of a specific coffee type.
Coffee
The Coffee class represents a type of coffee in the system.
It has the following methods:
__init__: Initializes a new coffee type with a name.
name: Returns the coffee type's name.
orders: Returns a list of orders for the coffee type.
customers: Returns a list of customers who have ordered the coffee type.
num_orders: Returns the number of orders for the coffee type.
average_price: Returns the average price of the coffee type.
Order
The Order class represents an order in the system.
It has the following methods:
__init__: Initializes a new order with a customer, coffee type, and price.
customer: Returns the customer who placed the order.
coffee: Returns the coffee type of the order.
price: Returns the price of the order.
Usage
To use the system, you can create customers, coffee types, and orders as follows:

python

Verify

Open In Editor
Edit
Copy code
# Create a customer
customer = Customer("John Doe")

# Create a coffee type
coffee = Coffee("Latte")

# Create an order
order = customer.create_order(coffee, 3.50)

# Get the customer's orders
orders = customer.orders()

# Get the coffee type's orders
coffee_orders = coffee.orders()

# Get the customer who has ordered the most of a specific coffee type
aficionado = Customer.most_aficionado(coffee)
Note
This is a basic implementation of a coffee shop management system, and it can be extended to include more features and functionality as needed.
