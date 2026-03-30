c, k=map(int, input().split())
money=10**k
result=((c+money//2)//money)*money
print(result)