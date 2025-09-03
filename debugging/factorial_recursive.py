#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function description:
        Recursively calculates the factorial of a given non-negative integer n.
        The factorial of n (written as n!) is the product of all positive integers from 1 to n.
        By definition, 0! = 1.

    Parameters:
        n (int): The non-negative integer for which the factorial will be computed.

    Returns:
        int: The factorial of n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)
