#!/usr/bin/python3
import sys

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

if len(sys.argv) != 2:
    print("Usage: python script.py <number>")
    sys.exit(1)

try:
    num = int(sys.argv[1])
    f = factorial(num)
    print(f)
except ValueError as e:
    print(f"Invalid input: {e}")
    sys.exit(1)

