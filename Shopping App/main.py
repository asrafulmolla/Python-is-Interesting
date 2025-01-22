from sellers import Sellers
from shop import Shop
from customer import Customer

# Example Usage:
shop = Shop("Tech Store")
seller = Sellers("John Doe", "john@example.com", shop)
customer = Customer("Jane Smith", "jane@example.com", shop)

# Adding products
seller.add_to_product("Laptop", 1000, 10)
seller.add_to_product("Mouse", 50, 20)

# Displaying products
seller.display_products()

# Customer ordering products
customer.order("Laptop", 2)
customer.order("Mouse", 5)
customer.order("Keyboard", 1)  # Not available


# Display updated products
customer.display_products()

customer.order("Laptop", 4)

customer.display_products()

seller.add_to_product("Laptop", 1500, 50)

customer.display_products()