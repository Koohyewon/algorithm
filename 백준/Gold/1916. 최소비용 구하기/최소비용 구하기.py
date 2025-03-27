import sys
import heapq
input = sys.stdin.readline

N = int(input())  
M = int(input())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))  

start_city, end_city = map(int, input().split())

def dijkstra(start):    
    d = [float('inf')] * (N + 1)  
    d[start] = 0  
    pq = [(0, start)]  

    while pq:
        cost, node = heapq.heappop(pq) 

        if cost > d[node]:  
            continue  
        
        for next, weight in graph[node]:
            new_cost = cost + weight
            if new_cost < d[next]:  
                d[next] = new_cost
                heapq.heappush(pq, (new_cost, next))
    
    return d

result = dijkstra(start_city)
print(result[end_city]) 
