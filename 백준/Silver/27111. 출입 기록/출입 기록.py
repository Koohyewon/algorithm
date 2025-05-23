import sys
input = sys.stdin.readline

N = int(input())
records = [tuple(map(int, input().split())) for _ in range(N)]

arr = [0] * 200001  # 0: 밖, 1: 안
missing = 0
for a, b in records:
    if b == 1:
        if arr[a]:            
            missing += 1    # 이미 안에 있는데 또 들어옴 -> 나가는 기록 누락
        arr[a] = 1
    else:
        if not arr[a]:            
            missing += 1    # 밖에 있는데 나감 -> 들어오는 기록 누락
        else:
            arr[a] = 0
            
missing += sum(arr) # 아직 안에 남아있는 사람들 -> 나가는 기록 누락
print(missing)