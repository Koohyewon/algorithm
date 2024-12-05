n = int(input())
grid = [input().strip() for _ in range(n)]

# 위치 저장
home = ""
end = ""
cookies = {"J": [], "C": [], "B": [], "W": []}

for i in range(n):
    for j in range(n):
        if grid[i][j] == "H":
            home = (j, i)
        elif grid[i][j] == "#":
            end = (j, i)
        elif grid[i][j] in "JCBW":
            cookies[grid[i][j]].append((j, i))

# 두 좌표 사이 거리 계산
def dist(start, end):
    return abs(start[0] - end[0]) + abs(start[1] - end[1])  # abs 절댓값

def min_distance(topping):
    min_dist = float('inf') 
    visited = [False] * 3 

    def backtrack(path, current_dist):
        nonlocal min_dist


        if len(path) == 3:
            total_dist = current_dist
            total_dist += dist(home, cookies[topping][path[0]])  # 집에서 첫 번째 토핑까지 거리
            for i in range(1, 3):
                total_dist += dist(cookies[topping][path[i - 1]], cookies[topping][path[i]])  # 중간에 있는 토핑들 간 거리
            total_dist += dist(cookies[topping][path[-1]], end)  # 마지막 토핑에서 끝까지 거리
            min_dist = min(min_dist, total_dist)
            return

        for i in range(3):  
            if not visited[i]:
                visited[i] = True
                backtrack(path + [i], current_dist)
                visited[i] = False

    backtrack([], 0)
    return min_dist

# 분야별 최소 거리 계산
results = {
    "Assassin": min_distance("J"),
    "Healer": min_distance("C"),
    "Mage": min_distance("B"),
    "Tanker": min_distance("W")
}

# 거리가 가장 작은 값을 찾고, 동일한 거리가 있으면 분야 이름 순으로 정렬
sorted_results = sorted(results.items(), key=lambda x: (x[1], x[0]))

print(sorted_results[0][0])
