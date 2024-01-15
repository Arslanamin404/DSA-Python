# Write a Recursive Func to print first n odd nums
def f1(n, current=1):
    if n > 0:
        if current % 2 != 0:
            print(current, end=" ")
            f1(n-1, current+2)


f1(5)
