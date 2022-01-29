n, W = [int(i) for i in input().split()]
items = []

if W == 0:
    print(0)
    quit()

for i in range(n):
    v, w = [int(i) for i in input().split()]
    if v == 0:
        continue
    items.append((v, w))

items.sort(key = lambda x: x[0]/x[1], reverse=True)

total = 0

for v, w in items:
    if W == 0:
        print(total)
        quit()
    q = min(w, W)
    total += q * v/w
    W = W - q

print(total)
