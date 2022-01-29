n = int(input())
ctr = 0
d = [10, 5, 1]

for i in d:
    if n >= i:
        ctr = ctr + n//i
        n = n % i
        if n == 0:
            print(ctr)
            quit()
            
