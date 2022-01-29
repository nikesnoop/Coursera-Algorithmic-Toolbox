a, b = [int(i) for i in input().split()]


def Euclidian(a, b):
    while (b):
        a, b = b, a % b

    return a


print(Euclidian(a, b))
