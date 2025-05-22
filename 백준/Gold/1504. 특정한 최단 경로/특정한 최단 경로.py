import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start, n, graph):
    dist = [INF] * (n + 1)
    dist[start] = 0
    hq = [(0, start)]

    while hq:
        cost, now = heapq.heappop(hq)
        if cost > dist[now]:
            continue
        for to, weight in graph[now]:
            if dist[to] > cost + weight:
                dist[to] = cost + weight
                heapq.heappush(hq, (dist[to], to))
    return dist

# 입력
n, e = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

# 각 정점에서의 최단 거리 구하기
dist_1 = dijkstra(1, n, graph)
dist_v1 = dijkstra(v1, n, graph)
dist_v2 = dijkstra(v2, n, graph)

# 두 가지 경우 비교
route1 = dist_1[v1] + dist_v1[v2] + dist_v2[n]  # 1 → v1 → v2 → N
route2 = dist_1[v2] + dist_v2[v1] + dist_v1[n]  # 1 → v2 → v1 → N

res = min(route1, route2)

print(res if res < INF else -1)
