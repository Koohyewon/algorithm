MAX_N = 100000
is_prime = [True] * (MAX_N + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(MAX_N ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, MAX_N + 1, i):
            is_prime[j] = False

def largest_prime(s):
    max_p = -1
    n = len(s)

    for i in range(n):
        for j in range(i + 1, n + 1):
            num = int(s[i:j])
            if num >= 2 and num <= MAX_N and is_prime[num]:
                max_p = max(max_p, num)
    
    return max_p

while True:
    s = input().strip()
    if s == '0':
        break
    print(largest_prime(s))
