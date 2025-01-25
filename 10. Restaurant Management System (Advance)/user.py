from abc import ABC
from orders import Order
from restaurent import Restaurant 
from food_item import FoodItem

class User(ABC):
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address

class Customer(User):
    def __init__(self, name, email, address):
        super().__init__(name, email, address)
        self.cart = Order()
        self.wallet = 0 
        self.past_orders = [] 

    def view_menu(self, restaurant):
        restaurant.menu.show_menu()  

    def add_to_cart(self, restaurant, item_name, quantity):
        item = restaurant.menu.find_item(item_name)  
        if item:
            if quantity > int(item.quantity):
                print('Item Quantity Exceeded!!')
            else:
                price = int(item.price) * quantity
                if price + self.cart.total_price > self.wallet:
                    print(f'Insufficient wallet balance. You need {price} but have only {self.wallet - self.cart.total_price} available.')
                else:
                    self.cart.add_item(item, quantity)
                    restaurant.menu.update_quantity(item_name, quantity)
                    print(f'{quantity} {item.name} added to the cart.')
        else: 
            print('Item not Found!')  

    def view_cart(self):
        print('******* View Cart *********')
        print('Name\tPrice\tQuantity')
        for item, quantity in self.cart.items.items():  
            print(f'{item.name}\t{item.price}\t{quantity}')
        print(f'Total Price: {self.cart.total_price}')
    
    def add_blance(self, amount):  
        if amount > 0:
            self.wallet += amount  
    
    def pay_bill(self):
        if self.cart.total_price>0:
            print(f'Total {self.cart.total_price} paid successfully...')
            self.wallet -= self.cart.total_price
            past_order = Order()
            past_order.items = self.cart.items.copy()
            self.past_orders.append(past_order)
            self.cart.clear()  
        else:
            print ('Empty Your Card')
    
    def view_past_order(self):
        if len(self.past_orders)==0:
            print('No past orders found.')
        else:
            print('******* View Past Orders *********')
            for i, order in enumerate(self.past_orders, start=1):
                print(f'Order {i}:')
                print('Name\tPrice\tQuantity')
                sum=0
                for item, quantity in order.items.items():
                    print(f'{item.name}\t{item.price}\t{quantity}')
                    sum+=(int(item.price) * int(quantity))
                print(f'Total Price: {sum}')
                print('-----------------------------------')

class CustomerNew(User):
    def __init__(self, name, email, address):
        super().__init__(name, email, address)

class Admin(User):
    def __init__(self, name, email, address):
        super().__init__(name, email, address)

    def add_customer(self, restaurant, custommer):
        restaurant.add_customer(custommer)  

    def view_customer(self, restaurant):
        restaurant.view_customers() 

    def add_new_item(self, restaurant, item):
        restaurant.menu.add_menu_item(item)  

    def remove_item(self, restaurant, item_name):
        restaurant.menu.remove_item(item_name)
        
    def view_menu(self, restaurant):
        restaurant.menu.show_menu() 
        
    def remove_customer(self, restaurant, custommer):
        restaurant.remove_customer(custommer) 
    
    def update_price(self, restaurant, item_name, update_rate):
        restaurant.menu.update_price(item_name,update_rate) 