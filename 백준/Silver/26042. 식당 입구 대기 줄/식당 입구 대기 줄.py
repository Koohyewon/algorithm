import sys
input=sys.stdin.readline

n = int(input())
arr = []	#줄
result = [0,0] #대기 학생수, 학생 끝번호
for _ in range(n):
    cmd = list(map(int,input().split()))
    if cmd[0] == 1:	
        arr.append(cmd[1])   
        
        if result[0] < len(arr):	
            result[0] = len(arr)
            result[1] = arr[-1]
        
        elif result[0] == len(arr):
            result[1] = min(result[1], arr[-1])     
    else:
        arr.pop(0)	

print(result[0], result[1])
