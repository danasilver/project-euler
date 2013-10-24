#!/usr/bin/env python

def main():
    """Return the product of a, b, c where a < b < c are members of a
    Pythagorean triplet and a + b + c = 1000."""

    # 1 .. 998 for each a, b, c
    # because 998 + 1 + 1 = 1000
    for a in range(1, 999):
        for b in range(1, 999):
            for c in range(1, 999):
                if a + b + c == 1000 and a**2 + b**2 == c**2:
                    return a * b * c

if __name__ == "__main__":
    print main()