def powerFunc(base, exp):
    if exp == 0:
        return 1
    else:
        return base*powerFunc(base, exp-1)


print(powerFunc(5, 2))
