def find_paths(graph, N):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if graph[i][k] and graph[k][j]:
                    graph[i][j] = 1
    return graph

N = int(input()) 
graph = [list(map(int, input().split())) for _ in range(N)]

graph = find_paths(graph, N)

for row in graph:
    print(" ".join(map(str, row)))
