n = int(input())
a = [int(i) for i in input().split()]
k = int(input())
b = [int(i) for i in input().split()]


def bin_search(r, k):
    l = 0
    global a
    m = l + (r - l) // 2
    while l <= r:
        mid = l + (r - l) // 2
        if a[mid] == i:
            if i == a[mid - 1]:
                r = mid - 1
            elif i != a[mid - 1] or mid - 1 < 0:
                return mid
        elif a[mid] < i:
            l = mid + 1
        else:
            r = mid - 1
    return -1


res = []
for i in b:
    res.append(bin_search(len(a) - 1, i))
print(*res)
