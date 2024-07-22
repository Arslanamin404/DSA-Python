# Script to create a list of N terms of fibonacci series

def fib(term):
    if term == 0 or term == 1:
        return term
    else:
        return fib(term-1)+fib(term-2)


def generate_terms(n):
    fibonacci_series_list = []
    start = 0
    while len(fibonacci_series_list) != n:
        fibonacci_series_list.append(fib(start))
        start += 1
    return fibonacci_series_list


if __name__ == "__main__":
    n = int(input("Number of Fibonacci Terms: "))
    print(generate_terms(n))
