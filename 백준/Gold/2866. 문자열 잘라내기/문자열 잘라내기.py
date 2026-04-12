import sys
input = sys.stdin.readline

r, c = map(int, input().split())

board = [input().strip() for _ in range(r)]

cols = []
for col in range(c):
    word = ""
    for row in range(r):
        word += board[row][col]
    cols.append(word)

cnt = 0

for cut in range(r):
    check = set()
    same = False
    
    for col in range(c):
        word = cols[col][cut:]  
        
        if word in check:
            same = True
            break
        
        check.add(word)
    
    if same:
        break
    
    cnt += 1

print(cnt - 1)