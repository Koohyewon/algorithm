from sys import stdin
n = int(stdin.readline())
count = 0

for a in range(1, n + 1):
    for b in range(a, n + 1):
        c = n - a - b
        
        if c < b:
            break
        
        if a + b > c:
            count += 1

print(count)