# Write a program to calculate the credit card balance after one year
# if a person only pays the minimum monthly payment required
# by the credit card company each month.
# balance is a variable with the outstanding balance on the credit card
# annual_interest_rate variable is the anual interest rate as a decimal
# monthly_payment_rate variable is the minimum monthly payment rate as decimal
# Monthly interest rate = (Annual interest rate) / 12.0
# Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
# Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
# Updated balance each month =
# (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

balance = float(input('Enter the outstanding balance: '))
annual_interest_rate = float(input('Enter the annual interest rate: '))
monthly_payment_rate = float(input(
    'Enter the minimuM monthly payment rate: '))
monthly_interest_rate = annual_interest_rate / 12

for _ in range(12):
    # Month unp bal = prev bal - min payment rate * prev bal
    balance = balance * (1 - monthly_payment_rate)
    # Updated bal month = month unp bal + month interest rate * month unp bal
    balance = balance * (1 + monthly_interest_rate)

print('Remaining balance:', round(balance, 2))
