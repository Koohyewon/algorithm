from collections import deque

def bfs(start, graph, n):
    visited = [False] * (n + 1)
    visited[start] = True

    q = deque([start])
    cnt = 0

    while q:
        now = q.popleft()

        for nxt in graph[now]:
            if not visited[nxt]:
                visited[nxt] = True
                cnt += 1
                q.append(nxt)

    return cnt


def solution(n, results):
    win = [[] for _ in range(n + 1)]
    lose = [[] for _ in range(n + 1)]

    for a, b in results:
        win[a].append(b)  
        lose[b].append(a) 

    answer = 0

    for i in range(1, n + 1):
        win_cnt = bfs(i, win, n)
        lose_cnt = bfs(i, lose, n)

        if win_cnt + lose_cnt == n - 1:
            answer += 1

    return answer