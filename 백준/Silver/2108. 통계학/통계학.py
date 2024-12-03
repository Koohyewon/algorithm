import sys
input = sys.stdin.readline

n = int(input())
nums = [int(input()) for i in range(n)]

print(round(sum(nums)/n))

nums.sort()
print(nums[n//2])

cnt = dict()
for i in nums:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1

max_nums = []

for i in cnt:
    if cnt[i] == max(cnt.values()):
        max_nums.append(i)

print(max_nums[0]) if len(max_nums) == 1 else print(max_nums[1])
    
print(max(nums)-min(nums))