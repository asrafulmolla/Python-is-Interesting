from menu import Menu

class Restaurant:
    def __init__(self, name):
        self.name = name
        self.customers = []  # customer database
        self.menu = Menu()

    def add_customer(self, customer):
        if self.find_customer(customer) is None:
            self.customers.append(customer)
        else:
            print('Customer Username Allready Exsit in Your Restaurant\nPlease Try Unique Username..')

    def view_customers(self):
        print('Customers List:')
        for cus in self.customers:
            print(f'Customers Name: {cus.name}, Email: {cus.email}, Address: {cus.address}')
            
    def remove_customer(self, customer_name):
        cus = self.find_customer(customer_name)
        if cus:
            self.customers.remove(cus)
            print('Customer deleted')
        else:
            print('Customer not found!')
            
    def find_customer(self, customer_name):
        for cus in self.customers:
            if cus.name.lower() == customer_name.lower():
                return cus
        return None