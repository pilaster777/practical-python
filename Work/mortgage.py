# mortgage.py
#
# Exercise 1.7
principal = 500000
rate = 0.05

total_paid = 0.0
extra_payment_start_month = input("extra_payment_start_month")
extra_payment_end_month = input("extra_payment_end_month")
extra_payment = input("extra_payment")

month = 0

while principal > 0:
    payment = 2684.11
    
    if int(extra_payment) > 0 and (int(extra_payment_start_month) <= int(month) <= int(extra_payment_end_month)):
        payment = payment + int(extra_payment)
    principal = principal * ( 1 + rate / 12 ) - payment
    total_paid = total_paid + payment
    month += 1
    
print('Total paid', round(total_paid,1))
print('Total time', month // 12,  " Year(s), ", month % 12, " Month(s) ..... or ",month," month(s)")