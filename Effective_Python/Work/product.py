

class Product:

    def __init__(self, name, quant, price) -> None:
        self.name = name
        self.quant = quant
        self.price = price

    def cost(self): 
        return self.quant *self.price



    
