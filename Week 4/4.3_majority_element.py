d = {}
n = int(input())
a = [int(i) for i in input().split()]

for i in a:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1

if max(d.values()) > n // 2:
    print(1)
else:
    print(0)
