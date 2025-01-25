class Menu:
    def __init__(self):
        self.items = []  # Menu database

    def add_menu_item(self, item):
        self.items.append(item)
        print ('Item Added....')

    def find_item(self, item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return item
        return None

    def remove_item(self, item_name):
        item = self.find_item(item_name)
        if item:
            self.items.remove(item)
            print('Item deleted')
        else:
            print('Item not found!')

    def show_menu(self):
        print('******** Menu *********')
        print('Name\tPrice\tQuantity')
        for item in self.items:
            print(f'{item.name}\t{item.price}\t{item.quantity}')
            
    def update_price(self, item_name, update_rate):
        item = self.find_item(item_name)
        if item:
            item.price=update_rate
            print('Price Updated')
        else:
            print('Item not found!')
            
    def update_quantity(self, item_name, quantity):
        item = self.find_item(item_name)
        if item:
            item.quantity = int(item.quantity) - quantity 
            if item.quantity <= 0:  
                self.remove_item(item_name)


