from collections import deque

def dslr(n, op):
    if op == 'D':
        return (n * 2) % 10000
    elif op == 'S':
        return 9999 if n == 0 else n - 1
    elif op == 'L':
        return (n % 1000) * 10 + n // 1000
    elif op == 'R':
        return (n % 10) * 1000 + n // 10

def bfs(A, B):
    queue = deque([A])
    visited = {A: ""}  

    while queue:
        num = queue.popleft()
        path = visited[num]
        
        if num == B:
            return path

        for op in "DSLR":
            new_num = dslr(num, op)
            if new_num not in visited: 
                visited[new_num] = path + op
                queue.append(new_num)

    return ""

T = int(input().strip())
results = []

for _ in range(T):
    A, B = map(int, input().split())
    results.append(bfs(A, B))

print("\n".join(results))
