# pcost.py
#
# Exercise 1.27
f = open('Data/portfolio.csv', 'rt')
headers = next(f).split(',')
cost = 0
for line in f:
    row = line.split(',')
    cost = cost + int(row[1]) * float(row[2])
print(f"Total cost: {cost}")

f.close()

