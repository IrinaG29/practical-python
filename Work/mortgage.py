# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
extra_payment = 1000
first_12_months = 1

while principal > 0:
    if first_12_months < 13:
        principal = principal * (1+rate/12) - payment - extra_payment
        total_paid = total_paid + payment + extra_payment
        first_12_months = first_12_months + 1
    else:
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment

print('Total paid', total_paid)
