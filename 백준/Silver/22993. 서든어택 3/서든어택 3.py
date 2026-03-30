n=int(input())
arr=list(map(int, input().split()))

jun=arr[0]
others=arr[1:]
others.sort()

for x in others:
    if jun>x:
        jun+=x
    else:
        print("No")
        exit()
print("Yes")