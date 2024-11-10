import sys

N, M = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

prefix_sum = [0] * (N + 1)
for i in range(1, N + 1):
    prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]

results = []
for _ in range(M):
    i, j = map(int, input().split())
    result = prefix_sum[j] - prefix_sum[i - 1]
    results.append(result)
    
print("\n".join(map(str, results)))