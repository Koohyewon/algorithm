n=int(input())
nums=list(map(int, input().split()))

arr=[[0,1000000000]] 

for i in range(n):
    arr.append([max(arr[i][0], nums[i]-arr[i][1]), min(arr[i][1], nums[i])])
    
for i in range(1, n+1):
    print(arr[i][0], end=" ")