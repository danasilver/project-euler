#! /usr/bin/env python3

from math import factorial

def main():
    """Compute the sum of the digits in 100!"""

    # Divide and conquer factorial algorithm in python3 is much faster
    return sum([int(i) for i in str(factorial(100))])

if __name__ == "__main__":
    print(main())