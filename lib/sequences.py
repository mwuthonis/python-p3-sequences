#!/usr/bin/env python3

def print_fibonacci(length):
    if length <= 0:
        print([])  # Print an empty list for length = 0
        return

    fib = [0, 1]
    while len(fib) < length:
        fib.append(fib[-1] + fib[-2])  # Fix indentation here

    print(fib[:length])  # Print the Fibonacci sequence

# Example usage
print_fibonacci(9)
