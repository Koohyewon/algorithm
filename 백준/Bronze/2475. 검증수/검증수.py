numbers = list(map(int, input().split()))

cnt = 0
for num in numbers:
    cnt += num ** 2

print(cnt % 10)
