from report import read_inventory


def recipt(filename):
    inv = read_inventory(filename)
    total = 0
    for pr in inv:
        total += pr.quant * pr.price
    
    return total

amount = recipt("Data/inventory.csv")

print(f"Your Bill Amount is : {amount}")
