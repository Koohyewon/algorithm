import heapq

def solution(n, works):
    if sum(works) <= n:
        return 0

    heap = [-work for work in works]
    heapq.heapify(heap)

    for _ in range(n):
        work = heapq.heappop(heap)  
        work += 1           
        heapq.heappush(heap, work)

    return sum(x * x for x in heap)