T=int(input())

for _ in range(T):
    n,m=map(int, input().split())
    a=list(map(int, input().split()))
    b=list(map(int, input().split()))
    
    b.sort()
    
    cnt=0
    for size_a in a:
        left, right = 0, m
        while left < right:
            mid = (left + right) // 2
            if b[mid] < size_a:
                left = mid + 1
            else:
                right = mid
        cnt += left
    
    print(cnt)            