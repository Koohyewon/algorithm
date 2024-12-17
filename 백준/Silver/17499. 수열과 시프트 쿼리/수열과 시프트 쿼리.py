import sys
from collections import deque

input = sys.stdin.readline

N, Q = map(int, input().split())

deq = deque(map(int, input().split()))
for _ in range(Q):
    cmd = list(map(int, input().split()))
    
    if cmd[0] == 1:        
        i, x = cmd[1] - 1, cmd[2] 
        deq[i] += x
    
    elif cmd[0] == 2:
        s = cmd[1]
        deq.rotate(s)  
        
    elif cmd[0] == 3:    
        s = cmd[1]
        deq.rotate(-s)  

print(" ".join(map(str, deq)))