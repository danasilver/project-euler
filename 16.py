#!/usr/bin/env python

from operator import __add__

def main():
    """Compute the sum of the digits of 2^1000."""
    return reduce(__add__, [int(i) for i in str(2**1000)])

if __name__ ==  "__main__":
    print main()