# report.py
#
# Exercise 2.4
import csv

def portfolio_cost(filename):
    '''Computes the total cost (shares*price) of a portfolio file'''
    portfolio = []
    total = 0.0
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = (row[0], int(row[1]), float(row[2]))
            portfolio.append(holding)
        for name, shares, price in portfolio:
            total += shares*price
    print(total)

portfolio_cost('Data/portfolio.csv')