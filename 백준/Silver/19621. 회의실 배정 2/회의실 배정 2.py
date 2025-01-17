n = int(input())

# 회의 정보
array = []

for _ in range(n):
  # 시작 시간, 끝나는 시간, 회의 인원
  array.append(list(map(int, input().split())))

# 회의시간 정렬(K번째 회의는 앞, 뒤 회의랑만 겹치고, 다른 회의랑은 겹치지 않는다는 조건)
array.sort()

#인원
dp = [0] * n
dp[0] = array[0][2] 

for i in range(1, n):
  dp[i] = max(dp[i - 1], dp[i - 2] + array[i][2])

print(dp[n - 1])