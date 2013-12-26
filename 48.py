#!/usr/bin/env python

from operator import __add__

def main():
    """Compute the last 10 digits of the series 1^1 + 2^2 + 3^3 + ... + 1000^1000."""
    
    return str(reduce(__add__, map(lambda i: i ** i, range(1, 1001))))[-10:]

if __name__ == "__main__":
    print main()