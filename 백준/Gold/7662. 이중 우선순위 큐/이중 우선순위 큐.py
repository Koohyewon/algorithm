import sys
import heapq

input = sys.stdin.readline

T = int(input().strip())
results = []

for _ in range(T):
    k = int(input().strip())
    min_heap = []
    max_heap = []
    
    visited = {}    
    for i in range(k):
        op, num = input().split()
        num = int(num)
        if op == 'I':           
            heapq.heappush(min_heap, (num, i))
            heapq.heappush(max_heap, (-num, i))
            visited[i] = True
        else:  
            if num == 1:  # 최대값 삭제
                while max_heap and not visited.get(max_heap[0][1], False):
                    heapq.heappop(max_heap)
                if max_heap:
                    _, idx = heapq.heappop(max_heap)
                    visited[idx] = False
            elif num == -1:  # 최소값 삭제
                while min_heap and not visited.get(min_heap[0][1], False):
                    heapq.heappop(min_heap)
                if min_heap:
                    _, idx = heapq.heappop(min_heap)
                    visited[idx] = False
    
    while min_heap and not visited.get(min_heap[0][1], False):
        heapq.heappop(min_heap)
    while max_heap and not visited.get(max_heap[0][1], False):
        heapq.heappop(max_heap)
    
    if not min_heap or not max_heap:
        results.append("EMPTY")
    else:
        max_val = -max_heap[0][0]
        min_val = min_heap[0][0]
        results.append(f"{max_val} {min_val}")

print("\n".join(results))
