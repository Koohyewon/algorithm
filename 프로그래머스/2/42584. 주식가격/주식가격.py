from collections import deque

def solution(prices):
    queue = deque()
    for i in range(len(prices)):
        queue.append((i, prices[i]))
    
    result = [0] * len(prices)
    
    while queue:
        idx, price = queue.popleft()
        for next_idx, next_price in queue:
            result[idx] += 1
            if next_price < price:
                break
    
    return result