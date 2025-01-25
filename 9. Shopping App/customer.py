from User import User

class Customer(User):
    def __init__(self, name, email, shop):
        super().__init__(name, email)
        self.shop = shop  # Associate customer with a shop

    def order(self, product_name, quantity):
        product_name = product_name.lower()  # Normalize product names for consistency
        if product_name in self.shop.products:
            if self.shop.products[product_name]['quantity'] < quantity:
                print(f"Insufficient stock. Available quantity: {self.shop.products[product_name]['quantity']}")
            else:
                bill = self.shop.products[product_name]['price'] * quantity
                print ('------------------------------------------')
                print("Your Order: ")
                print (f'Product Name\tQuantity\tTotal Price')
                print (f'{product_name}\t\t{quantity}\t\t{quantity*self.shop.products[product_name]['price']}')
                print ('------------------------------------------')
                print(f"                    Total Bill: {bill}")
                self.shop.products[product_name]['quantity'] -= quantity
        else:
            print ("********************************************")
            print(f"{product_name.capitalize()} is not available in {self.shop.name}.")
            print ("********************************************")

    def display_products(self):
        # Display all products in the shop
        print ("********************************************")
        print(f"Products in {self.shop.name}:")
        print(f"Product Name\tUnit Price\tQuantity")
        for name, details in self.shop.products.items():
            if details['quantity']>0:
                print(f"{name.capitalize()}\t\t{details['price']}\t\t{details['quantity']}")
        print ("********************************************")
