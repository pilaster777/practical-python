# pcost.py
#
# Exercise 1.30

def portfolio_cost(filename):
    f = open(filename, 'rt')
    headers = next(f).split(',')
    cost = 0
    for line in f:
        row = line.split(',')
        cost = cost + int(row[1]) * float(row[2])
    f.close()
    return cost
cost = portfolio_cost('Data/portfolio.csv')
print(f"Total cost: {cost}")