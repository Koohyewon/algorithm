n=int(input())
k=int(input())

def k_sejun(n):
    i = 2
    while i <= n:
      if i > k:
         return False   # 나누는 소수가 k보다 크면 안됨

      if n % i == 0:
         n /= i
      else:
         i += 1   # 나누어 떨어지지 않으면 다른 나누어 떨어지는 수 찾기위해 +1

    return True 

cnt = 0
for N in range(2, n+1):
    if k_sejun(N):
        cnt += 1
print(cnt+1) # 1도 K세준수에 해당하니까 +1