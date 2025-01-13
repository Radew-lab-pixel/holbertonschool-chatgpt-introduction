#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

if len(sys.argv) > 1:
    try:
        num = int(sys.argv[1])
        f = factorial(num)
        print(f)
    except ValueError:
        print("Please provide a valid integer.")
else:
    print("Please provide a number as an argument.")