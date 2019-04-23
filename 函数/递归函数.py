# 初视算法

# f(n) = f(n - 1) + f(n - 2)


def func(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return func(n-1) + func(n-2)


print(func(7))
