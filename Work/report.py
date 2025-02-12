# report.py
#
# Exercise 2.15: A practical enumerate() example
import csv
from pprint import pprint


def read_prices(pricelist_filename):

    prices = {} # Initial empty dict

    with open(pricelist_filename, 'rt') as f:
        rows = csv.reader(f)
        #headers = next(rows)
        
        for row in rows:
            if row != []:
                try:
                    prices[row[0]]= float(row[1])
                except ValueError:
                    print(f'ValueError: Couldn\'t convert: ', end = ' ')
    return(prices)


def portfolio_cost(stock_filename,pricelist_filename):
    '''Computes the total cost (shares*price) of a portfolio file'''
    res = []
    portfolio = []
    t_gain_loss = 0.0
    total = 0.0

    with open(stock_filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)

        for row_c, row in enumerate(rows, start=1):
            hldg = {}
            try:
                hldg['name'], hldg['shares'], hldg['price'] = row[0], int(row[1]), float(row[2])
            except ValueError:
                print(f'Row {row_c}: Couldn\'t convert: {row}')
            if hldg != {}:
                portfolio.append(hldg)
        prices = read_prices(pricelist_filename)
        
        for i in range(len(portfolio)):
            shares = int(portfolio[i]['shares'])
            old_price = float(portfolio[i]['price'])
            new_price = float(prices[portfolio[i]['name']])
            name = portfolio[i]['name']

            change = new_price - old_price
            gain_loss = shares * change
            t_gain_loss += gain_loss
            total += shares * new_price
            
            res.append((name,shares,new_price,change))
    
    if t_gain_loss < 0:
        print(f'\nTotal worth of stock: {total:10.2f} \tIt\'s a loss of {t_gain_loss:10.2f}\n\n')
    else:
        print(f'Current value of my stock: \t{total:10.2f} \nIt\'s a win of \t\t\t{t_gain_loss:10.2f}\n\n')
    
    return(res)


def make_report(stock_filename, pricelist_filename):
    listi = portfolio_cost(stock_filename,pricelist_filename)
    return listi

headers = ('Name', 'Shares', 'Price', 'Change')
ct = 0 
sep = '----------'
for name, shares, price, change in make_report('Data/missing.csv','Data/prices.csv'):
        price = '$'+str(price)
        if ct % 10 == 0:
            print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
            print(f'{sep:>10s} {sep:>10s} {sep:>10s} {sep:>10s}')
        print(f'{name:>10s} {shares:>10d} {price:>10s} {change:>10.2f}')
        ct +=1
       


    
