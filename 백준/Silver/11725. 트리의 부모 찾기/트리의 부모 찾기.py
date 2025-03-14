import sys
from collections import deque

def find_parents(N, edges):
    tree = [[] for _ in range(N + 1)]
    parent = [0] * (N + 1)

    for a, b in edges:
        tree[a].append(b)
        tree[b].append(a)

    queue = deque([1])
    while queue:
        node = queue.popleft()
        for child in tree[node]:
            if parent[child] == 0:  
                parent[child] = node
                queue.append(child)

    return parent[2:]  

N = int(sys.stdin.readline().strip())
edges = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N - 1)]
result = find_parents(N, edges)
sys.stdout.write("\n".join(map(str, result)) + "\n")
