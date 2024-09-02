# https://www.hackerrank.com/contests/mountblue-technologies/challenges/staircase

import math
import os
import random
import re
import sys

# Complete the 'staircase' function below.
# The function accepts INTEGER n as parameter.

# Approach - 1
def staircase1(n):
    # Write your code here
    for i in range(1,n+1):
        print(" " * (n-i) + "#" * i)

# Summary
# Time Complexity: O(n^2)
# Space Complexity: O(n)

# Approach - 2
def staircase2(n):
    for i in range(1,n+1):
        print(f"{' ' * (n-i)}{'#' * i}")

# Summary
# Time Complexity: O(n^2)
# Space Complexity: O(n)

# Approach - 3 (Triangle)
def staircase3(n):
    for i in range(1,n+1):
        print(" " * (n-i) + "# " * i)

# Summary
# Time Complexity: O(n^2)
# Space Complexity: O(n)

# Approach - 4 (Recursion)
def print_line(n,i):
    if i>n:
        return
    print(" " * (n-i) + "#" * i)
    print_line(n,i+1)

def staircase4(n):
    print_line(n,1)

# Summary
# Time Complexity: O(n^2)
# Space Complexity: O(n)

# Approach - 5 (reverse staircase - iteration)
def reverse_staircase(n):
    for i in range(n,0,-1):
        print(" " * (n-i) + "#" * i)

# Summary
# Time Complexity: O(n^2)
# Space Complexity: O(1)

# Approach - 6 (reverse staircase - recursion)
def reverse_staircase1(n,i=0):
    if i==n:
        return
    print(" " * i + "#" * (n-i))
    reverse_staircase1(n,i+1)

# Summary
# Time Complexity: O(n^2)
# Space Complexity: O(n)


if __name__ == '__main__':
    n1 = int(input("Enter number for Approach - 1: ").strip())
    staircase1(n1)
    n2 = int(input("Enter number for Approach - 2: ").strip())
    staircase2(n2)
    n3 = int(input("Enter number for Approach - 3 (Triangle): ").strip())
    staircase3(n3)
    n4 = int(input("Enter number for Approach - 4 (Recursion): ").strip())
    staircase4(n4)
    n5 = int(input("Enter number for Approach - 5 (Reverse Staircase): ").strip())
    reverse_staircase(n5)
    n6 = int(input("Enter number for Approach - 6 (Reverse Staircase - Recursion): ").strip())
    reverse_staircase(n6)