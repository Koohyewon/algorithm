import sys

N = int(sys.stdin.readline().strip())  
arr = list(map(int, sys.stdin.readline().strip().split()))  

arr.sort()

value = arr[2] - arr[0] 
for i in range(4, N, 2):
    value += arr[i] - arr[i-1]  
    
ans = value
for i in range(2, N - 1, 2):  
    value -= (arr[i] - arr[i - 2])
    value -= (arr[i + 2] - arr[i + 1])
    value += (arr[i - 1] - arr[i - 2])
    value += (arr[i + 2] - arr[i])
        
    ans = min(ans, value)

print(ans)