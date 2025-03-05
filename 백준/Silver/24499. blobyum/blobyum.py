n, k = map(int, input().split())
a = list(map(int, input().split()))

a = a * 2

now_sum = sum(a[:k])
max_sum = now_sum

for i in range(1, n):
    now_sum = now_sum - a[i - 1] + a[i + k - 1]
    max_sum = max(max_sum, now_sum)

print(max_sum)