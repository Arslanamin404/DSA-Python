def f1(n, current=2):
    if n > 0:
        if (current % 2 == 0):
            f1(n-1, current+2)
            print(current, end=" ")


f1(5)
