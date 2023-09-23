#!/usr/bin/python3
# -*- coding: utf-8 -*-

def fib(n):
    """Print a Fibonacci sequence up to n"""
    a, b = 0,1
    while a < n:
        print(a, end=' ')
        a,b = b, a+b
    print()

def main():
    """Call functions"""
    m = int(input("Enter last number: "))
    fib(m)

main()
