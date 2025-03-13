def backtrack(path, used):
    if len(path) == M:
        print(*path)
        return
    
    prev = -1
    for i in range(N):
        if not used[i] and prev != numbers[i]:
            used[i] = True
            path.append(numbers[i])
            backtrack(path, used)
            path.pop()
            used[i] = False
            prev = numbers[i]

N, M = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort()

used = [False] * N
backtrack([], used)
