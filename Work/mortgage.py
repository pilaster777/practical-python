# mortgage.py
#
# Exercise 1.17: f-strings
principal = 500000
rate = 0.05

total_paid = 0.0

if input('Extra payment? Y/n ') == 'Y':
    extra_payment_start_month = int(input('extra_payment_start_month '))
    extra_payment_end_month = int(input('extra_payment_end_month '))
    extra_payment = int(input('extra_payment '))
else:
    extra_payment_start_month = 0
    extra_payment_end_month = 0
    extra_payment = 0

month = 0

while principal > 0:
    payment = 2684.11
    if extra_payment_start_month != [None,'',0] or extra_payment_end_month != [None,'',0]:
        if extra_payment > 0: 
            if extra_payment_start_month <= month <= extra_payment_end_month:
                payment = payment + extra_payment
    if principal < payment:
        payment = principal * ( 1 + rate / 12 )
    principal = principal * ( 1 + rate / 12 ) - payment
    total_paid = total_paid + payment
    month += 1
    
    print(f'Month \t{month} \tTotal payment: \t{total_paid:0.2f} \tprincipal: \t{principal:0.2f}')
    
print(f'Total paid: \t{total_paid:0.2f}')
print(f'Months \t\t{month}')
    
