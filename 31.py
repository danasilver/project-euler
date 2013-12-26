#!/usr/bin/env python3

def main():
    """Return the number of ways to make 2 pounds (200p)
    using the eight British coins."""

    coins, limit = [1, 2, 5, 10, 20, 50, 100, 200], 200
    ways = [0 for i in range(limit + 1)]
    ways[0] = 1

    for i in range(0, len(coins)):
        for j in range(coins[i], limit + 1):
            ways[j] += ways[j - coins[i]]

    return ways[-1]

if __name__ == "__main__":
    print(main())