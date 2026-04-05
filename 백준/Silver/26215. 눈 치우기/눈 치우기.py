n = int(input())
arr = list(map(int, input().split()))

time = 0

while True:
    arr.sort(reverse=True)
    
    if arr[0] == 0:
        break
    
    if len(arr) >= 2 and arr[1] > 0:
        arr[0] -= 1
        arr[1] -= 1
    else:
        arr[0] -= 1
    
    time += 1
    
    if time > 1440:
        print(-1)
        exit()

print(time)