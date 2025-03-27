n = int(input())
arr = list(map(int, input().split()))

left = 0
count = 0

for right in range(n):
    if right > 0 and arr[right - 1] > arr[right]:
        left = right  # 오름차순이 깨지면 left를 갱신
    
    count += (right - left + 1)  

print(count)