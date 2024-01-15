def f1(n, current=2):
    if n > 0:
        if current % 2 == 0:
            print(current)
            f1(n-1, current+2)

f1(5)