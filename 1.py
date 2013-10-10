#!/usr/bin/env python

def main():
    """Return the sum of all multiples of 3 or 5 below 1000."""
    sum = 0
    for x in range(1000):
        if (x % 3 == 0) or (x % 5 == 0):
            sum += x
    return sum

if __name__ == "__main__":
    print main()