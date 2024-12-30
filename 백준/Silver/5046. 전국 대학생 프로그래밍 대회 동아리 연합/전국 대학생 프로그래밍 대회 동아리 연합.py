import sys
input=sys.stdin.readline

N, B, H, W = map(int, input().split())

min_cost = float('inf')
for _ in range(H):
    p = int(input())  # 1인당 비용
    availability = list(map(int, input().split()))  # 주별 투숙 가능 인원
    # 주별로 참가자 수용 가능 여부            
    for available in availability:
        if available >= N: 
            cost = N * p  
            if cost <= B: 
                min_cost = min(min_cost, cost)
                
if min_cost == float('inf'):
    print("stay home")
else:
    print(min_cost)
