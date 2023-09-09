from product import Product

class GSTProduct(Product):
    def panic(self):
        self.sell(self.quant)

    def cost(self):
        return 1.25*self.quant *self.price

c = GSTProduct("Mint",100,210.1) #child class obj
print(c.cost())
print(c.quant)

p = Product("Mint",100,210.1) #parent class obj
print(p.cost())
print(p.quant)