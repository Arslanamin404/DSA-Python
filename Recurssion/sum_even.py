def sumEven(n):
    if n == 1:
        return 2
    else:
        return (2*n) + sumEven(n-1)


print(sumEven(2))
