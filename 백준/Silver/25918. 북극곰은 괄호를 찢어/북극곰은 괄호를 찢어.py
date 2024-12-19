import sys
input = sys.stdin.readline

N = int(input())
S = input().rstrip()
day = 0
total = 0
for char in S:
    if char == '(':
        total += 1
    else:
        total -= 1
    if abs(total) > day:
        day = abs(total)
if total == 0:
    print(day)
else:
    print(-1)