#Referred to: https://stackoverflow.com/questions/42944323/finding-the-last-digit-of-partial-sum-of-fibonacci-series
m, n = [int(i) for i in input().split()]

def sum_fib(m, n):
    if m > n:
        return

    a = [0, 1]
    for i in range(2, 60):
        a.append(a[i - 1] + a[i - 2])

    m = m % 60
    n = n % 60
    if n < m:
        n += 60

    su = 0
    for j in range(m, n + 1):
        su += a[j % 60]

    return su % 10

print(sum_fib(m, n))
