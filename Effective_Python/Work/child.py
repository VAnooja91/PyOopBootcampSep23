from product import Product

class GSTProduct(Product):

    def __init__(self, name,quant,price, tax): #redefining init 
        super().__init__(name,quant,price)  # calling parent class init
        self.tax = tax

    def panic(self):
        self.sell(self.quant)

    def cost(self):
        actual_cost = super().cost()
        return (self.tax*actual_cost)%100

c = GSTProduct("Mint", 100, 210.1, 25) #child class obj
print(c.cost())
print(c.quant)

p = Product("Mint", 100, 210.1) #parent class obj
print(p.cost())
print(p.quant)