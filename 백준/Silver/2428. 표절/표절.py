n = int(input())
arr = list(map(int, input().split()))

arr.sort()

cnt = 0
left = 0

for right in range(n):
    while arr[left] < 0.9 * arr[right]:
        left += 1

    cnt += (right - left)

print(cnt)