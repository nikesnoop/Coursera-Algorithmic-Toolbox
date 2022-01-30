n = int(input())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]

a.sort()
b.sort()
s = 0
for i in range (n):
    s += a[i] * b[i]

print(s)
