#!/usr/bin/env python

def factorial(n):
    """Return n!"""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    """Compute the number of routes through a 20x20 grid,
    from top left to bottom right only moving right and down."""

    n, k = 20 + 20, 20

    # n C k or in this case 40 C 20
    return factorial(n) / (factorial(k) * factorial(n - k))

if __name__ == "__main__":
    print main()