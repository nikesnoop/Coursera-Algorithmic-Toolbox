n = int(input())

if n <= 1:
    print(n)
    quit()

def fibo(n):
    a, b = 0, 1
    c = 0
    for i in range (n-1):
        c = a + b
        b, a = c, b
    return c

print(fibo(n))
