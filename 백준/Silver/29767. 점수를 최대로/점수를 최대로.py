import sys
input = sys.stdin.readline

n, k = map(int, input().split())
data = list(map(int, input().split()))

total = 0
prefix = []
for a in data:
    total += a
    prefix.append(total)  

prefix.sort(reverse=True)
print(sum(prefix[:k]))
