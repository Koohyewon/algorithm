import sys
input = sys.stdin.readline

n, m, v = map(int, input().split())
arr = list(map(int, input().split()))

for i in range(m):
  k = int(input())

  if k < n:
    print(arr[k])
  else:
    tmp = (k - n) % (n - v + 1)
    print(arr[v - 1 + tmp])