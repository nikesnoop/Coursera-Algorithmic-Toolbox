n = int(input())
arr = [[0 for i in range(2)] for j in range(n)]

for i in range(n):
    a = [int(i) for i in input().split()]
    for j in range(2):
        arr[i][j] = a[j]

arr.sort(key=lambda item: item[1])

results = [arr[0][1]]
for segment in arr:
    if segment[0] > results[-1]:
        results.append(segment[1])

print(len(results))
print(*results)
