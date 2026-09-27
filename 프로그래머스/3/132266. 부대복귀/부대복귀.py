from collections import deque

def solution(n, roads, sources, destination):
    graph = []
    for i in range(n + 1):
        graph.append([])

    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)

    distance = [-1] * (n + 1)
    distance[destination] = 0

    queue = deque()
    queue.append(destination)
    while queue:
        now = queue.popleft()
        for next_area in graph[now]:
            if distance[next_area] == -1:
                distance[next_area] = distance[now] + 1
                queue.append(next_area)

    answer = []
    for source in sources:
        answer.append(distance[source])

    return answer