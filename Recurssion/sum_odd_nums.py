def sumOdd(n):
    if n == 1:
        return n
    else:
        return (2*n) - 1 + sumOdd(n-1)


print(sumOdd(2))
