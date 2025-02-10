# report.py
#
# Exercise 2.6 and 2.7
import csv
from pprint import pprint


def read_prices(filename):

    prices = {} # Initial empty dict

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            #print(row)
            if row != []:
                prices[row[0]]= float(row[1])
            else:continue
            
    return(prices)


def portfolio_cost(filename):
    '''Computes the total cost (shares*price) of a portfolio file'''

    portfolio = []
    t_gain_loss = 0.0
    total = 0.0

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)

        for row in rows:
            hldg = {}
            hldg['name'], hldg['shares'], hldg['price'] = row[0], int(row[1]), float(row[2])
            portfolio.append(hldg)
        
        prices = read_prices('Data/prices.csv')
        
        for i in range(len(portfolio)):
            t_gain_loss += int(portfolio[i]['shares'])*(float(portfolio[i]['price']) - float(prices[portfolio[i]['name']]))
            total += int(portfolio[i]['shares'])*float(portfolio[i]['price'])

    if t_gain_loss < 0:
        print(f'total: {total} \tIt\'s a loss of {t_gain_loss}')
    else:
        print(f'Current value of my stock: \t{total} \nIt\'s a win of \t\t\t{t_gain_loss}')

portfolio_cost('Data/portfolio.csv')
