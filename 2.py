#!/usr/bin/env python

def main():
    """Return the sum of the even valued terms of the Fibonacci sequence whose values do not exceed 4000000."""
    x, y, sum = 1, 1, 0
    while x < 4000000:
        fib = x + y
        x = y
        y = fib
        if fib % 2 == 0:
            sum += fib
    return sum

if __name__ == "__main__":
    print main()