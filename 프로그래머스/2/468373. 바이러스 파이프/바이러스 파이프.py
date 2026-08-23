from collections import deque

def solution(n, infection, edges, k):
    graph = [[] for _ in range(n)]

    for x, y, t in edges:
        x -= 1
        y -= 1

        graph[x].append((y, t))
        graph[y].append((x, t))

    answer = 1

    def spread(infected, pipe_type):
        q = deque()

        for i in range(n):
            if infected[i]:
                q.append(i)

        visited = [False] * n

        while q:
            cur = q.popleft()

            if visited[cur]:
                continue

            visited[cur] = True

            for nxt, t in graph[cur]:
                if t == pipe_type and not infected[nxt]:
                    infected[nxt] = True
                    q.append(nxt)

    def dfs(count, infected):
        nonlocal answer

        if count == k:
            answer = max(answer, sum(infected))
            return

        for pipe_type in range(1, 4):
            next_infected = infected[:]

            spread(next_infected, pipe_type)

            dfs(count + 1, next_infected)

    infected = [False] * n
    infected[infection - 1] = True

    dfs(0, infected)

    return answer