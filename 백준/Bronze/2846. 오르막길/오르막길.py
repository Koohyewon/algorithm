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

# for문으로 모든 원소를 한 번씩만 확인하므로 시간복잡도: O(N), 1 ≤ N ≤ 1000