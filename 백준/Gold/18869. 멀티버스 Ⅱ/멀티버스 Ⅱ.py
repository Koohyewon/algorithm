import sys
from collections import Counter
input = sys.stdin.readline

M, N = map(int, input().split())
universes = []

for _ in range(M):
    planets = list(map(int, input().split()))
    # 각 행성 크기를 등수로 변환
    sorted_planets = sorted(set(planets))
    rank = {v: i for i, v in enumerate(sorted_planets)}
    signature = tuple(rank[x] for x in planets)
    universes.append(signature)

# 우주쌍의 개수 세기
counter = Counter(universes)
result = 0
for cnt in counter.values():
    if cnt > 1:
        result += cnt * (cnt - 1) // 2

print(result)