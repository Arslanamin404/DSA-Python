# create a list of N prime nums
from math import *


def is_prime(num):
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


if __name__ == "__main__":
    n = int(input("How many prime numbers you want: "))
    prime_numbers = []

    number = 2  # because 0 & 1 are not prime so their is no reason to start from 0
    count = 0

    while count <= n:
        if is_prime(number):
            prime_numbers.append(number)
            count += 1
        number += 1

    print(f"\nFirst {n} Prime Numbers are: {prime_numbers}\n")
