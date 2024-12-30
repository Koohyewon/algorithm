n=int(input())
cnt=[0] * (n+1)

if n>=0:
    cnt[0] = 1
if n>=1:
    cnt[1] = 1

for i in range(2, n + 1):
    cnt[i] = (cnt[i-1] + cnt[i-2] + 1) % 1000000007
print(cnt[n])
