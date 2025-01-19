from menu import Menu

class Restaurant:
    def __init__(self, name):
        self.name = name
        self.employees = []  # Employee database
        self.menu = Menu()

    def add_employee(self, employee):
        self.employees.append(employee)

    def view_employee(self):
        print('Employee List:')
        for emp in self.employees:
            print(f'Employee Name: {emp.name}, Phone: {emp.phone}, Email: {emp.email}, Address: {emp.address}')
