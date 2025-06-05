import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))  # 무방향 그래프니까 양쪽 연결

# DFS 함수
def dfs(node, accumulated):
    visited[node] = True
    global max_dist, farthest_node
    if accumulated > max_dist:
        max_dist = accumulated
        farthest_node = node

    for neighbor, weight in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor, accumulated + weight)

# 1. 루트(1번)에서 가장 먼 노드 찾기
visited = [False] * (n + 1)
max_dist = 0
farthest_node = 0
dfs(1, 0)

# 2. 그 노드에서 다시 DFS
visited = [False] * (n + 1)
max_dist = 0
dfs(farthest_node, 0)

print(max_dist)
