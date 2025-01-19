from abc import ABC
from orders import Order
from restaurent import Restaurant
from food_item import FoodItem

class User(ABC):
    def __init__(self, name, phone, email, address):
        self.name = name
        self.email = email
        self.address = address
        self.phone = phone

class Customer(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.cart = Order()  # Corrected typo

    def view_menu(self, restaurant):
        restaurant.menu.show_menu()

    def add_to_cart(self, restaurant, item_name, quantity):
        item = restaurant.menu.find_item(item_name)
        if item:
            if quantity>item.quantity:
                print ('Item Quantity Exceeded!!')
            else:
                self.cart.add_item(item, quantity)
                print('Item Added')
        else:
            print('Item not Found!')

    def view_cart(self):
        print('******* View Cart *********')
        print('Name\tPrice\tQuantity')
        for item, quantity in self.cart.items.items():
            print(f'{item.name}\t{item.price}\t{quantity}')
        print(f'Total Price: {self.cart.total_price}')
    
    def pay_bill(self):
        print (f'Total {self.cart.total_price} paid successfully...')
        self.cart.clear()
        
class Employee(User):
    def __init__(self, name, phone, email, address, age, designation, salary):
        super().__init__(name, phone, email, address)
        self.age = age
        self.designation = designation
        self.salary = salary

class Admin(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)

    def add_employee(self, restaurant, employee):
        restaurant.add_employee(employee)

    def view_employee(self, restaurant):
        restaurant.view_employee()

    def add_new_item(self, restaurant, item):
        restaurant.menu.add_menu_item(item)

    def remove_item(self, restaurant, item_name):
        restaurant.menu.remove_item(item_name)
        
    def view_menu(self, restaurant):
        restaurant.menu.show_menu()

# Example Usage
# mamar_res = Restaurant("Mamar Restaurant")

# item1 = FoodItem('Pizza', 12.45, 10)
# item2 = FoodItem('Burger', 10.00, 30)
# admin = Admin('Rahim', 4567, 'rahim@gmail.com', 'Rangpur')
# admin.add_new_item(mamar_res, item1)
# admin.add_new_item(mamar_res, item2)

# customer1 = Customer('Karim', 1234, 'karim@gmail.com', 'Dhaka')
# customer1.view_menu(mamar_res)

# item_name=input('Enter Item name: ')
# item_quantity=int(input('Enter Item Quantity: '))
# customer1.add_to_cart(mamar_res, item_name, item_quantity)
# customer1.view_cart()
