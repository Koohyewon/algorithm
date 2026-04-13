import sys
input = sys.stdin.readline


n,k=map(int, input().split())
dolls = list(map(int, input().split()))

left = 0
cnt_lion = 0
result = n + 1

for right in range(n):
    if dolls[right] == 1:
        cnt_lion += 1
        
    while cnt_lion >= k:
        result = min(result, right - left + 1)
        if dolls[left] == 1:
            cnt_lion -= 1
        left += 1

if result == n + 1:
    print(-1)
else:
    print(result)