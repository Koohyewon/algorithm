from itertools import permutations

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def count_primes(nums):
    primes = set()
    for r in range(1, len(nums)+1):
        for perm in permutations(nums, r):
            n = int(''.join(perm))
            if is_prime(n):
                primes.add(n)
    return len(primes)

t = int(input())
for _ in range(t):
    nums = list(input().strip())
    print(count_primes(nums))