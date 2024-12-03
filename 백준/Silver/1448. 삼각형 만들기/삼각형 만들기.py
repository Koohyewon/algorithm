import sys
n=int(sys.stdin.readline())
straw=sorted([int(sys.stdin.readline()) for _ in range(n)], reverse=True)

res=-1
for i in range(n-2): #뒤에서 2번째까지 왔으면 뒤에 비교할 빨대가 부족하므로 n-2회 실행
    if straw[i]<straw[i+1]+straw[i+2]:
        res=straw[i]+straw[i+1]+straw[i+2]
        break
print(res)