def fac(n):
    if n == 1 or n == 0:
        return 1
    return n * fac(n - 1)


print(fac(50))


def fac2(n):
    if n == 1 or n == 0:
        return 1
    f = 1
    for i in range(1, n + 1):
        f = f * i
    return f


print(fac2(50))
