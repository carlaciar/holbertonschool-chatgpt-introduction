#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1   # decrease n to avoid infinite loop
    return result

if len(sys.argv) < 2:
    print("Usage: {} <number>".format(sys.argv[0]))
    sys.exit(1)

try:
    num = int(sys.argv[1])
    if num < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        f = factorial(num)
        print(f)
except ValueError:
    print("Please provide a valid integer.")
