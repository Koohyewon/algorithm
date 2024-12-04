
n=int(input())
nums=list(map(int, input().split()))

arr=[[0,1000000000]] 

for i in range(1, n+1):
    arr.append([max(arr[i-1][0], nums[i-1]-arr[i-1][1]), min(arr[i-1][1], nums[i-1])])
    
for i in range(1, n+1):
    print(arr[i][0], end=" ")