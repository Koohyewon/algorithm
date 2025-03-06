from collections import deque

def bfs(ladders, snakes):
    board = {i: i for i in range(1, 101)}  
    for x, y in ladders:
        board[x] = y  
    for u, v in snakes:
        board[u] = v 
    
    queue = deque([(1, 0)])  
    visited = set()
    visited.add(1)
    
    while queue:
        pos, rolls = queue.popleft()
        
        if pos == 100:  
            return rolls
        
        for dice in range(1, 7): 
            next_pos = pos + dice
            if next_pos <= 100:
                next_pos = board[next_pos] 
                
                if next_pos not in visited:
                    visited.add(next_pos)
                    queue.append((next_pos, rolls + 1))

N, M = map(int, input().split())
ladders = [tuple(map(int, input().split())) for _ in range(N)]
snakes = [tuple(map(int, input().split())) for _ in range(M)]

print(bfs(ladders, snakes))
