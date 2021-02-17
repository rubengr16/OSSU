# Given a position on the serie in order,
# obtain its value on the Fibonacci Serie:
# 1, 1, 2, 3, 5, 8, 13, ..., ((n - 1) + (n - 2))
def fib(x):
    if x == 0 or x == 1:  # Base Case: x = 0 or x = 1 positions, value 1
        return 1
    else:
        return fib(x - 1) + fib(x - 2)
