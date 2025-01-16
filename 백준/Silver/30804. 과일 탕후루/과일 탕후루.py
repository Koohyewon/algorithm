from collections import defaultdict

n = int(input())
fruit = list(map(int, input().split()))
s, e = 0, 0
count = defaultdict(int)
max_count = 0

while e < n:
    count[fruit[e]] += 1
    
    while len(count.keys()) > 2:
        count[fruit[s]] -= 1
        if count[fruit[s]] == 0:
            del count[fruit[s]]
        s += 1
    e += 1
    max_count = max(max_count, sum(count.values()))
print(max_count)