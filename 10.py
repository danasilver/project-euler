#!/usr/bin/env python

from math import sqrt

def is_prime(x):
    """Determine if a given x is prime."""

    if x < 3:
        return bool(x == 2)
    if x % 2 == 0:
        return False
    if any((x % i == 0) for i in range(3, int(sqrt(x)) + 1, 2)):
        return False
    return True

def main():
    """Return the sum of all primes below two million."""
    return sum([i if is_prime(i) else 0 for i in range(2, 2000000)])

if __name__ == "__main__":
    print main()