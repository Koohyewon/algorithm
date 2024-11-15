import sys

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]

for i in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [0] * (n + 1)
cnt = 0

def dfs(v):
    stack = [v]
    visited[v] = 1
    while stack:
        node = stack.pop()
        for neighbor in graph[node]:
            if visited[neighbor] == 0:
                visited[neighbor] = 1
                stack.append(neighbor)

for i in range(1, n + 1):
    if visited[i] == 0:
        dfs(i)
        cnt += 1

print(cnt)