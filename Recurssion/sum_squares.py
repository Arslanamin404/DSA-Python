def sumSquare(n=None):
    if n == 1 or n == 0:
        return n
    return n*n + sumSquare(n-1)


print(sumSquare(5))
