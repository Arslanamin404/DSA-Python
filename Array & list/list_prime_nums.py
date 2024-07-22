# Script to create a list of N prime numbers
import math

def is_prime(num):
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True


def generate_prime_numbers(n):
    prime_numbers_list = []
    num = 2
    while len(prime_numbers_list) != n:
        if is_prime(num):
            prime_numbers_list.append(num)
        num += 1
    return prime_numbers_list


if __name__ == "__main__":
    n = int(input("Number of Prime Numbers: "))

    print(generate_prime_numbers(n))
