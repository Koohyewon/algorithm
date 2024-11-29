import sys

n=int(sys.stdin.readline())
V=list(map(int, sys.stdin.readline().split()))

speed=0
total=0
for v in V[::-1]:
    if speed < v:
        speed+=1

    else:
        speed=v
    total+=speed
    
print(total)