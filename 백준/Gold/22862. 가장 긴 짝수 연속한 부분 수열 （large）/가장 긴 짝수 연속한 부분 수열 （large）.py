n, k = map(int, input().split())
arr = list(map(int, input().split()))

l, r = 0, 0
odd_count = 0
result = 0
while r < n:
    if odd_count <= k:
        if arr[r] % 2 == 1: 
            odd_count += 1
        r += 1
    else:
        if arr[l] % 2 == 1:
            odd_count -= 1
        l += 1
    result = max(result, r - l - odd_count)

print(result)
