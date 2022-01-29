n = int(input())

n = (n+2) % 60

if n == 1:
    print(0)
    quit()
if n == 0:
    print(9)
    quit()

a, b = 0, 1
c = 0
for i in range(2, n+1):
    c = a + b
    c = c % 10
    b, a = c, b
if c!=0:
    print(c-1)
else:
    print(9)
