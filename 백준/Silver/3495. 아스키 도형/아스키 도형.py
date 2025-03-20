h, w = map(int, input().split())  # 높이, 너비
grid = [list(input()) for _ in range(h)]

full = 0  # 1칸 면적 개수
half = 0  # 0.5칸 면적 개수

for i in range(h):
    inside = 0  
    for j in range(w):
        if grid[i][j] in "/\\":
            half += 1
            inside += 1
        elif inside % 2 == 1:
            full += 1

print(full + (half // 2))
