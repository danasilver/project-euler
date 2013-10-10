#!/usr/bin/env python

def main():
    """Return the largest prime factor of 600851475143."""
    x, factors, divisor = 600851475143, [], 2
    while x > 1:
        while x % divisor == 0:
            factors.append(divisor)
            x /= divisor
        divisor += 1
    return max(factors)

if __name__ == "__main__":
    main()