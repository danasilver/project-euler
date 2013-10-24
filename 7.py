#!/usr/bin/env python

from math import sqrt

def isPrime(x):
    """Determine if a given x is prime."""
    prime_check_ceil = int(sqrt(x))
    for i in range(2, prime_check_ceil + 1):
        if x % i == 0:
            return False
    return True

def main():
    """Return the 10001st prime."""
    test_number = 2
    nth_prime = 1
    while nth_prime <= 10001:
        if isPrime(test_number):
            nth_prime += 1
        test_number += 1
    return test_number - 1

if __name__ == "__main__":
    print main()