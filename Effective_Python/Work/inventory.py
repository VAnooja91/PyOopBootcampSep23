from product import Product
import fileparse as fp

class Inventory:
    def __init__(self):
        #self._products = products 
        self._products = []
        #inpython convenction: _product implies private variable
    def __iter__(self):
        return self._products.__iter__()
    
    def total_cost(self):
        return sum(p.cost() for p in self._products)
    
    def append(self, prod):
        self._products.append(prod)

    @classmethod
    def from_csv(cls, filename):
        self = cls()
        inv_list = fp.parse_csv(filename, 
                     select=['name', 'quant', 'price'],
                     types=[str, int, float])

        for pr_dict in inv_list:
            prod = Product(pr_dict['name'], 
                           pr_dict['quant'], 
                           pr_dict['price']
                          )
            self.append(prod)

        return self

# Main
inv = Inventory.from_csv('Data/inventory.csv')

    