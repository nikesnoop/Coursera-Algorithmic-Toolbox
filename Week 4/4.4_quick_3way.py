import random

n = int(input())
a = [int(i) for i in input().split()]


def randomized_quick_sort(l, r):
    global a
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    m1, m2 = partition3(a, l, r)
    randomized_quick_sort(l, m1 - 1);
    randomized_quick_sort(m2 + 1, r);


def partition3(a, l, r):
    x, j, t = a[l], l, r
    i = j

    while i <= t:
        if a[i] < x:
            a[j], a[i] = a[i], a[j]
            j += 1

        elif a[i] > x:
            a[t], a[i] = a[i], a[t]
            t -= 1
            i -= 1
        i += 1
    return j, t


randomized_quick_sort(0, len(a) - 1)
print(*a)
