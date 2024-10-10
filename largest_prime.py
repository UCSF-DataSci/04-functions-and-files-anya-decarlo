#!/usr/bin/env python3
"""
Largest Prime Fibonacci Number

Write a program that takes a number as an argument, finds the *Fibonacci* numbers less than that number, and prints the largest prime number in the list. 

	- Use command-line arguments to specify the upper limit 
	- Implement a function to check if a number is prime
	- Import and use the Fibonacci generating function from problem 1 as a module

Task: Find the largest prime Fibonacci number less that 50000
"""

# You're on your own for this one. Good luck!

#!/usr/bin/env python3
import sys
import math
from fibonnaci import fibonnanci  # Import the function

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def find_largest_prime_fibonacci(limit):
    fib_list = fibonnanci(limit)  # Using the imported function
    prime_fibs = [n for n in fib_list if is_prime(n)]
    
    if prime_fibs:
        return max(prime_fibs)
    return None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 largest_prime_fibonacci.py <upper_limit>")
        sys.exit(1)
    
    try:
        upper_limit = int(sys.argv[1])
    except ValueError:
        print("Please provide a valid integer as the upper limit.")
        sys.exit(1)
    
    largest_prime_fib = find_largest_prime_fibonacci(upper_limit)
    
    if largest_prime_fib is not None:
        print(f"The largest prime Fibonacci number less than {upper_limit} is: {largest_prime_fib}")
    else:
        print(f"No prime Fibonacci numbers found below {upper_limit}.")