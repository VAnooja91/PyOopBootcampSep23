'''
    Displays gain or loss of inventory
'''

import csv
import fileparse as fp
from product import Product
from tableformat import (TableFormatter,
                         TextTableFormatter,
                         CSVTableFormatter,
                         create_formatter, 
                         FormateError
                        )

def read_prices(filename:str) -> dict:
    '''
        Reads a prices csv file
        Returns a dictionary with value for each product
    '''
    inv_list = fp.parse_csv(filename, types=[str, float], has_headers=False)
    return dict(inv_list)

#def read_inventory(filename: str) -> list[tuple]:
def read_inventory(filename):
    '''
        Reads a csv file
        Returns a list of dictionaries [ for each row ]
    '''
    #return fp.parse_csv(filename, 
    inv = fp.parse_csv(filename, 
                 select=['name', 'quant', 'price'],
                 types=[str, int, float])

    # Add code here
    # convert inv .. which is a list of dictionaries
    # to a list of Product instances
    # Return that list of Product instances
    inventory = [ Product(pr_dict['name'], pr_dict['quant'], pr_dict['price'])
                  for pr_dict in inv
                ]
    return inventory

def make_report(inventory, prices):
    report = list()
    for prod in inventory:
        name = prod.name
        quant = prod.quant
        latest_price = prices[name]
        change = latest_price - prod.price
        report.append( (name, quant, latest_price, change) )

    return report


def print_report(report, formatter):
    headers = ('Name', 'Quantity', 'Price', 'Change')
    #print('%10s %10s %10s %10s' % headers)
    #dashes = tuple(['-' * 10] * 4)
    #print('%10s %10s %10s %10s' % dashes)
    formatter.headings(headers)

    for name,quant,price,change in report:
        #print('%10s %10d %10.2f %10.2f' % r)
        rowdata = [name, str(quant), f'{price:.2f}', f'{change:.2f}']
        formatter.row(rowdata)


def inventory_report(inventory_file, prices_file, frmt = 'txt'):
    inventory = read_inventory(inventory_file)
    prices = read_prices(prices_file)
    report = make_report(inventory, prices)
    try:
        formatter = create_formatter(frmt)
    except FormateError as e:
        print(e)
        print(f"*********Falling back to Text Format**********")
        formatter = create_formatter('txt')
    print_report(report, formatter)


def main():
    import sys
    if len(sys.argv) != 4:
        raise SystemExit(f'Usage: {sys.argv[0]} invfile pricesfile frmt')

    inv_file = sys.argv[1]
    prices_file = sys.argv[2]
    frmt = sys.argv[3]
    inventory_report(inv_file, prices_file,frmt)

# Main starts from here
if __name__ == "__main__":
    main()