class Order:
    def __init__(self):
        self.items = {}

    def add_item(self, item, quantity):
        if item in self.items:
            self.items[item] += quantity  # Increment quantity
        else:
            self.items[item] = quantity  # Add new item

    def remove_item(self, item):
        if item in self.items:
            del self.items[item]
    @property
    def total_price(self):
        return sum(int (item.price) * int (quantity) for item, quantity in self.items.items())

    def clear(self):
        self.items = {}