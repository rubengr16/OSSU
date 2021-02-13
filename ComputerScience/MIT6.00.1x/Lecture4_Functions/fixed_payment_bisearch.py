# Write a program that calculates the minimum fixed monthly payment needed
# in order pay off a credit card balance within 12 months.
# By a fixed monthly payment, we mean a single number which does not change
# each month, but instead is a constant amount that will be paid each month.
# balance variable is the outstanding balance
# annual_interest_rate variable is the annual interest rate as a decimal

balance = float(input('Enter the outstanding balance: '))
annual_interest_rate = float(input('Enter the annual interest rate: '))
lower_bound = balance / 12
upper_bound = (balance * 1 + annual_interest_rate) / 12
fixed_payment = (lower_bound + upper_bound) / 2
epsilon = 0.001

while abs(balance - (fixed_payment * 12)) > epsilon:
    if balance - (fixed_payment * 12) < 0:
        upper_bound = fixed_payment
    else:
        lower_bound = fixed_payment
    fixed_payment = (lower_bound + upper_bound) / 2


print('Lowest Payment:', round(fixed_payment, 2))
