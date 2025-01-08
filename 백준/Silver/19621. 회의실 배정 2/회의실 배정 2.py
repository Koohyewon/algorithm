def max_participants(n, meetings):
    meetings.sort(key=lambda x: x[1])
    dp = [0] * n
    dp[0] = meetings[0][2]

    for i in range(1, n):

        include = meetings[i][2]

        for j in range(i - 1, -1, -1):
            if meetings[j][1] <= meetings[i][0]:
                include += dp[j]
                break
     
        dp[i] = max(dp[i - 1], include)

    return dp[-1]

n = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(n)]

print(max_participants(n, meetings))
