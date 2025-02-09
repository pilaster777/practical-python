# pcost.py
#
# Exercise 1.33
import csv
import sys

def portfolio_cost(filename):
    f = open(filename, 'rt')
    rows = csv.reader(f)
    headers = next(rows)
    cost = 0
    for row in rows:
        cost = cost + int(row[1]) * float(row[2])
    f.close()
    return cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost('Data/portfolio.csv')
print(f"Total cost: {cost}")