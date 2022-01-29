a, b = [int(i) for i in input().split()]


def GCD(a, b):
    while (b):
        a, b = b, a % b

    return a


def LCM(a, b):
    if a==0 and b==0:
        return 0
    return (a*b)/GCD(a,b)


print(int(LCM(a,b)))
