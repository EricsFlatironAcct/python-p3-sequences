#!/usr/bin/env python3

def print_fibonacci(length):
    if length==0:
        print("[]")
    else:
        fib_list = []
        fib_list.append(0)
        if length > 1:
            fib_list.append(1)
            for n in range(2, length):
                fib_list.append(fib_list[n-2]+fib_list[n-1])
        print(fib_list)