n,m=map(int, input().split())
a=list(map(int, input().split()))
b=set(map(int, input().split()))

result = [i for i in a if i not in b]
result.sort()

print(len(result))
if result:
    print(' '.join(map(str, result)))

