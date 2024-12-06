from itertools import permutations

n = int(input())
grid = [input().strip() for _ in range(n)]
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

def dist(start, end):
    return abs(start[0] - end[0]) + abs(start[1] - end[1])

def min_distance(topping, home, end, cookies):
    locations = cookies[topping]
    
    # 3개 쿠키 위치의 모든 경우
    min_dist = float('inf')
    for perm in permutations(range(len(locations)), 3):
        # 집 -> 1번 쿠키 -> 2번 쿠키 -> 3번 쿠키 -> 쿠키크루삥뽕
        current_dist = (
            dist(home, locations[perm[0]]) +
            dist(locations[perm[0]], locations[perm[1]]) +
            dist(locations[perm[1]], locations[perm[2]]) +
            dist(locations[perm[2]], end)
        )
        min_dist = min(min_dist, current_dist)
    
    return min_dist

results = {
    "Assassin": min_distance("J", home, end, cookies),
    "Healer": min_distance("C", home, end, cookies),
    "Mage": min_distance("B", home, end, cookies),
    "Tanker": min_distance("W", home, end, cookies)
}

sorted_results = sorted(results.items(), key=lambda x: (x[1], x[0]))
print(sorted_results[0][0])