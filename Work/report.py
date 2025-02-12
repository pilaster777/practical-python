# report.py
#
# Exercise 2.15: A practical enumerate() example
import csv


def read_prices(pricelist_filename):

    prices = {} 

    with open(pricelist_filename, 'rt') as f: # file mustn't contain headers
        rows = csv.reader(f)
                
        for row in rows:
            if row != []:   # exclude empty rows
                try:        # avoid Errors because of missing vaues in pricelist
                    prices[row[0]]= float(row[1])
                except ValueError:
                    print(f'ValueError: Couldn\'t convert: ', end = ' ')
    return(prices)      #{'AA': 9.22, 'AXP': 24.85, ......  'WMT': 49.74, 'XOM': 69.35}


def portfolio_cost(stock_filename,pricelist_filename):
    '''Computes the total worth (shares*price) of a portfolio file and the actual gain/loss'''
    
    portfolio = []
    total = 0.0

    with open(stock_filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)    # skip header row and save headers

        for row_c, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            
            try:
                nshares = int(record['shares'])
                price = float(record['price'])
                total += nshares * price
            except ValueError:pass
                #print(f'Row {row_c}: Couldn\'t convert: {row}')
            if record != {}:  #exclude empty dicts
                portfolio.append(record)
        print("Total worth of portfolio:",total)
        
    
    
    
    return(portfolio)


def make_report(stock_filename, pricelist_filename):            #
    res = []
    t_gain_loss = 0                                                           
    record = portfolio_cost(stock_filename,pricelist_filename)
    
    prices = read_prices(pricelist_filename)
    for rowno,row in enumerate(record):     
        try:
            shares = int(row['shares'])
            old_price = float(row['price'])
            new_price = float(prices[row['name']])
        except ValueError:
            print(f'Row {rowno}: Bad row: {row}')
        
        change = new_price - old_price
        gain_loss = shares * change
        t_gain_loss += gain_loss
        
        res.append((row['name'],shares,new_price,change))

    if t_gain_loss < 0:
        t_gain_loss = t_gain_loss * -1
        print(f'\n\tIt\'s a loss of {t_gain_loss:10.2f}\n\n')
    else:
        print(f'\n\nIt\'s a win of \t\t\t{t_gain_loss:10.2f}\n\n')
    return res

headers = ('Name', 'Shares', 'Price', 'Change')
ct = 0 
sep = '----------'
for name, shares, price, change in make_report('Data/portfoliodate.csv','Data/prices.csv'):
        price = '$'+str(price)
        if ct % 10 == 0:                    # print out with headers every 10 rows
            print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
            print(f'{sep:>10s} {sep:>10s} {sep:>10s} {sep:>10s}')
        print(f'{name:>10s} {shares:>10d} {price:>10s} {change:>10.2f}')
        ct +=1
       


    
