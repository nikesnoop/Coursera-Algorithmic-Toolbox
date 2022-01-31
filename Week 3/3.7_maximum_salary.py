n = int(input())
numbers = [int(i) for i in input().split()]


def IsGreaterOrEqual(i, highest):
    return int(str(i) + str(highest)) >= int(str(highest) + str(i))


def largestNumber(nos):
    res = []
    while nos:
        highest = 0
        for i in nos:
            if IsGreaterOrEqual(i, highest):
                highest = i
        res.append(highest)
        nos.remove(highest)
    return res


print(*largestNumber(numbers), sep='')
