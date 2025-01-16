import sys
input = sys.stdin.readline
 
#ax값을 지정해주고 이 값보다 작거나 같은 경우에만 책을 위로 옮기면 된다. 

books = [int(input()) for _ in range(int(input().strip('\n')))]
max = books[0]
cnt = 0
for i in books[1:]:
    if i > max:
        if max + 1 != i:
            cnt += 1
        max = i
    else:
        cnt += 1
print(cnt)