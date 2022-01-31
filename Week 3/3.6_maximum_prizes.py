n = int(input())
if n == 1:
    print(1)
    print(1)
    quit()

temp, prizes = n, []

for i in range(1, n+1):
    if temp > 2 * i:
        prizes.append(i)
        temp -= i
    else:
        prizes.append(temp)
        break

print(len(prizes))
print(*prizes)
