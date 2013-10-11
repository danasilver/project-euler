#!/usr/bin/env python

def main():
    n = 1
    while True:
        if all(map(lambda x: n % x == 0, range(11, 21))):
            return n
        else:
            n += 1

if __name__ == "__main__":
    print main()