# 0,1,1,2,3,5,8,13,. . .
def fib(n):
    if n == 0:
        return n
    elif n == 1 or n == 2:
        return 1
    return fib(n-1)+fib(n-2)


print(fib(7))
