import sys
input = sys.stdin.readline

n = int(input())
dic = {}

for _ in range(n):
    name = input().rstrip()
    if name in dic:
        dic[name] += 1
    else:
        dic[name] = 1
        
for _ in range(n-1):
    name = input().rstrip()
    dic[name] -= 1
    
for i in dic:
    if dic[i]:
        print(i)
        break