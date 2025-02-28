import sys
n = int(sys.stdin.readline())
dic = {}

for i in range(2*n-1):
    name = sys.stdin.readline().strip()
    if name in dic:
        dic[name] += 1
    else:
        dic[name] = 0
for i in dic:
    if dic[i] % 2 == 0:
        print(i)
        break