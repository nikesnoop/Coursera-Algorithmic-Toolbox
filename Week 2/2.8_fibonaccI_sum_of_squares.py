#TLE but this is my submission. I couldn't understand optimal solution

n = int(input())

if n <= 1:
    print(n)
    quit()


def fibo(n):
    a, b = 0, 1
    c = 0
    arr = []
    for i in range(n):
        c = a + b
        c = c % 10
        arr.append(c)
        b, a = c, b
    return arr


res = fibo(n)
print((res[n-1]*res[n-2])%10)
