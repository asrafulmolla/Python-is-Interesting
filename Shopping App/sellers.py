from User import User

class Sellers(User):
    def __init__(self, name, email, shop):
        super().__init__(name, email)
        self.shop = shop  # Associate seller with a shop

    def add_to_product(self, product_name, price, quantity):
        product_name = product_name.lower()  # Normalize product names for consistency
        if product_name in self.shop.products:
            # Update the existing product
            self.shop.products[product_name]['quantity'] += quantity
            self.shop.products[product_name]['price'] = price  # Update price if necessary
        else:
            # Add a new product
            self.shop.products[product_name] = {'price': price, 'quantity': quantity}

    def display_products(self):
        # Display all products in the shop
        print ("********************************************")
        print(f"Products in {self.shop.name}:")
        print(f"Product Name\tUnit Price\tQuantity")
        for name, details in self.shop.products.items():
            print(f"{name.capitalize()}\t\t{details['price']}\t\t{details['quantity']}")
        print ("********************************************")