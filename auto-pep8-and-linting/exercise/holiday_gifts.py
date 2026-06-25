'''
This code takes in a list of prices
It adds the price of all items less than 25 dollars then adds tax
Returns the total price
'''

import numpy as np

def calculate_total_price(filename):
    '''calculate_total_price
    takes in a file
    adds up the cost of all items less than 25 dollars and adds tax
    returns the total price
    '''
    with open(filename, encoding="utf-8") as f:
        gift_costs = f.read().split('\n')

    gift_costs = np.array(gift_costs).astype(int)  # convert string to int

    total_price = 0

    # total price is the sum of all items less than 25 plus tax
    total_price = np.sum(np.where(gift_costs < 25, gift_costs, 0)) * 1.08

    return total_price


if __name__ == "__main__":
    print(calculate_total_price('gift_costs.txt'))
