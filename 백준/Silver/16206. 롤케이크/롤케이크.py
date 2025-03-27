import sys
input = sys.stdin.readline

N, M = map(int, input().split()) 
cakes = list(map(int, input().split()))

cakes.sort(key=lambda x: (x % 10, x))

answer = 0 

for cake in cakes:
    pieces = cake // 10  

    if cake % 10 == 0: 
        if pieces - 1 <= M:
            answer += pieces
            M -= pieces - 1
        else:
            answer += M
            M = 0
    else:  
        if pieces <= M:
            answer += pieces
            M -= pieces
        else:
            answer += M
            M = 0

print(answer)
