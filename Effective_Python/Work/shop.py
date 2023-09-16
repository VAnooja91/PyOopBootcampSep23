from report import read_inventory


def recipt(filename):
    inv = read_inventory(filename)
    
    return inv.total_cost()

amount = recipt("Data/inventory.csv")

print(f"Your Bill Amount is : {amount}")
