class Product(object):
    def __init__(self, price, item_name, weight, brand, cost):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = 'for sale'
    def sell(self):
        self.status = 'sold'
        return self
    def add_tax(self, tax):
        # note: tax should be passed in as a decimal, so 1 + tax would each 100% the full cost plus the %tax on the price
        return self.price * (1 + tax)
    def return_item(self, reason):
        if reason == 'defective':
            self.status = 'defective'
            self.price = 0
            return self
        elif reason == 'returned in box':
            self.status = 'for sale'
            return self
        elif reason == 'box opened':
            self.status = 'used'
            # note: price * 0.8 is equivalent to a 20% discount for used items
            self.price *= 0.8
            return self
    def display_info(self):
        info = self.__dict__  
        for key in info:
            print key , ":" , info[key]
        return self

product1 = Product(15, 'notebook', '2oz', 'Mead', 1)
product1.display_info()