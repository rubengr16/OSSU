# Write a program that calculates the minimum fixed monthly payment needed
# in order pay off a credit card balance within 12 months.
# By a fixed monthly payment, we mean a single number which does not change
# each month, but instead is a constant amount that will be paid each month.
# balance variable is the outstanding balance
# annual_interest_rate variable is the annual interest rate as a decimal

balance = float(input('Enter the outstanding balance: '))
annual_interest_rate = float(input('Enter the annual interest rate: '))
monthly_interest_rate = annual_interest_rate / 12
fixed_payment = -10
temp = balance

while temp > 0:
    fixed_payment += 10
    temp = balance
    for _ in range(12):
        temp = (temp - fixed_payment) * (1 + monthly_interest_rate)


print('Lowest Payment:', fixed_payment)
