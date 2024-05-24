#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        return []
    elif length == 1:
        return [0]
    
    fib = [0, 1]
    for i in range(2, length):
        fib.append(fib[-1] + fib[-2])
    return fib
length = 1
print(print_fibonacci(length))

# index 0 + index 1 = index 3


