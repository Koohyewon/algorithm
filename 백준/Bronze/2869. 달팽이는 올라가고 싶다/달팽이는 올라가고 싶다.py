import sys
input=sys.stdin.readline

a, b, v = map(int,input().split())

if (v - b) % (a - b) == 0:
    days = (v - b) // (a - b)
else:
    days = (v - b) // (a - b) + 1

print(days)