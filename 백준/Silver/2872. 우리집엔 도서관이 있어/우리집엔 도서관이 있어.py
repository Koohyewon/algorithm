import sys
N = int(sys.stdin.readline())
book_lst = []
for i in range(N):
    book_lst.append(int(sys.stdin.readline()))

maxbook = max(book_lst)

idx = book_lst.index(maxbook)
answer = len(book_lst)-idx-1
for book in book_lst[:idx][::-1]:
    if book == maxbook - 1:
        maxbook = book
    else:
        answer += 1
print(answer)