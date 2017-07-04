class Store(object):
    def __init__(self, products, location, owner):
        self.products = products
        self.location = location
        self.owner = owner
    def add_product(self, new_product):
        self.products.append(new_product)
        return self
    def remove_product(self, removed_product):
        product_index = self.products.index(removed_product)
        self.products.pop(product_index)
        return self
    def inventory(self):
        for item in self.products:
            print item
        return self

# Test out the class & functions
new_store = Store(['apples', 'bananas', 'cherries', 'durian'], 'Chicago', 'Mariano')
print "Inventory test"
new_store.inventory()
print '=' * 50
print "Add 'eggplant' then re-check inventory"
new_store.add_product('eggplant').inventory()
print '=' * 50
print "Remove 'cherries' then re-check inventory"
new_store.remove_product('cherries').inventory()
