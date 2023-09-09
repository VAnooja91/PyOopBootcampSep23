from product import Product

class GSTProduct(Product):
    def panic(self):
        self.sell(self.quant)

    def cost(self):
        pass

p = GSTProduct("Mint",100,210.1)
p.sell(10)

print(p.quant)