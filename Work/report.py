# report.py
#
# Exercise 2.5
import csv
from pprint import pprint

def portfolio_cost(filename):
    '''Computes the total cost (shares*price) of a portfolio file'''

    portfolio = []
    total = 0.0

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)

        for row in rows:
            holding = {}
            holding['name'], holding['shares'], holding['price'] = row[0], int(row[1]), float(row[2])
            portfolio.append(holding)

        for i in range(len(portfolio)):
            total += int(portfolio[i]['shares'])*float(portfolio[i]['price'])

    print(total)

portfolio_cost('Data/portfolio.csv')