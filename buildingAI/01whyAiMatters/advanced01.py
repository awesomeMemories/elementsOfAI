#!/usr/bin/env python3
#Factorial function.
# factorial for any non-negative integer n, 
# factorial is defined as 1 * 2 * 3 * 4 * 5 = 120
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(6))
