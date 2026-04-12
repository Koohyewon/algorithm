n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

left = max(arr)
right = sum(arr)

def check(k):
    cnt = 1
    money = k

    for x in arr:
        if money < x:
            cnt += 1
            money = k
        money -= x

    return cnt <= m

while left <= right:
    mid = (left + right) // 2

    if check(mid):
        right = mid - 1
    else:
        left = mid + 1

print(left)