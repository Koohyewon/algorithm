from collections import deque

a, b, n, m = map(int, input().split())
dp = dict()       
dp[n] = 0              
queue = deque([n])     


while queue:
    current = queue.popleft()
    move = [
        current + 1, current - 1,
        current + a, current - a,
        current + b, current - b, 
        current * a, current * b    
    ]

    for val in move:
        if 0 <= val <= 100000 and val not in dp:
            dp[val] = dp[current] + 1          
            queue.append(val)                

    if m in dp:
        break
        
print(dp[m])
