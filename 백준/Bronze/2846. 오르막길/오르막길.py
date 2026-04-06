n=int(input())
heights=list(map(int, input().split()))

max_up=0
current_up=0
for i in range(n-1):
    if heights[i+1]>heights[i]:
        current_up+=heights[i+1]-heights[i]
        max_up=max(max_up, current_up)
        
    else:
        current_up=0
        
print(max_up)