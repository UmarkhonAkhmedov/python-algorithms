x = 500
y = 2000


def recursive_product(x, y):
    if y == 0:
        return 0
    elif x < y:
        return recursive_product(y, x)
    return x + recursive_product(x, y-1)


print(x*y)
print(recursive_product(x, y))
