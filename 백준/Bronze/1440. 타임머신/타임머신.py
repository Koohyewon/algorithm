from itertools import permutations

a, b, c = input().split(':')
nums = [int(a), int(b), int(c)]

count = 0
for h, m, s in permutations(nums):
    if 1 <= h <= 12 and 0 <= m <= 59 and 0 <= s <= 59:
        count += 1

print(count)