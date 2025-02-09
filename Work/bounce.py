# bounce.py
#
# Exercise 1.5
height = 100 #unit is meter
b_rate = 3/5 # bouncing rate
for i in range(10):
    height = height * b_rate
    print(round(height,4))