import sys
inpur=sys.stdin.readline

n=int(input())
scores=[]

for _ in range(n):
    scores.append(float(input()))

bottom7=sorted(scores)[:7]

for i in bottom7:
    print(f"{i:.3f}")