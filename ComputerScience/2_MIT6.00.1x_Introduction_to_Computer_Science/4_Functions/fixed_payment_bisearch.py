# Write a program that calculates the minimum fixed monthly payment needed
# in order pay off a credit card balance within 12 months.
# By a fixed monthly payment, we mean a single number which does not change
# each month, but instead is a constant amount that will be paid each month.
# balance variable is the outstanding balance
# annual_interest_rate variable is the annual interest rate as a decimal

balance = float(input('Enter the outstanding balance: '))
annual_interest_rate = float(input('Enter the annual interest rate: '))
lower_bound = balance / 12
upper_bound = (balance * (1 + annual_interest_rate / 12) ** 12) / 12
fixed_payment = (lower_bound + upper_bound) / 2
epsilon = 0.001
temp = None  # Auxiliar variable to control the remaining debt

while temp is None or abs(temp) > epsilon:
    # While temp is not initialized or debt is greater than money precission
    if temp is not None:  # if temp is initialized
        if temp < 0:  # if the guess is too big
            upper_bound = fixed_payment - 0.01  # Avoids using the same guess
        else:  # otherwise, the guess is too low
            lower_bound = fixed_payment + 0.01  # Avoids using the same guess
        fixed_payment = (lower_bound + upper_bound) / 2

    temp = balance
    for _ in range(12):  # # Calculates the year's evolution of the debt
        temp = (temp - fixed_payment) * (1 + annual_interest_rate / 12)


print('Lowest Payment:', round(fixed_payment, 2))
