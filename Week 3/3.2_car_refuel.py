d = int(input())
m = int(input())
n = int(input())
stops = [int(i) for i in input().split()]
stops.sort()


def compute_min_refills(d, m, n, stops):
    num_refill, curr_refill, limit = 0, 0, m
    while limit < d:
        if curr_refill >= n or stops[curr_refill] > limit:
            return -1
        while curr_refill < n - 1 and stops[curr_refill + 1] <= limit:
            curr_refill += 1
        num_refill += 1
        limit = stops[curr_refill] + m
        curr_refill += 1

    return num_refill


print(compute_min_refills(d, m, n, stops))
