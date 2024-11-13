import sys
T = int(sys.stdin.readline())
result = [0] * T

for i in range(T):
    n = int(sys.stdin.readline())
    dic = {}
    
    for _ in range(n):
        clothes = sys.stdin.readline().split()
        category = clothes[1]
        if category in dic:
            dic[category] += 1
        else:
            dic[category] = 1
            
    C = 1
    for count in dic.values():
        C *= (count + 1)
    result[i] = C - 1  

for res in result:
    print(res)