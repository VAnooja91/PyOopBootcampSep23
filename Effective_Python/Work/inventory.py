class Inventory:
    def __init__(self, products):
        self._products = products 
        #inpython convenction: _product implies private variable
    def __iter__(self):
        return self._products.__iter__()

    def total_cost(self):
        return sum(p.cost() for p in self._products)
