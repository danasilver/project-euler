#!/usr/bin/env python

from operator import __add__

def main():
    """Return the sum of the first 100 natural numbers squared less\
    the sum of the square of the first 100 natural numbers"""
    return sum(range(1, 101))**2 - reduce(__add__, map(lambda x: x**2, range(1, 101)))

if __name__ == "__main__":
    print main()