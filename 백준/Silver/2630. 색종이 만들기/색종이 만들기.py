import sys
input=sys.stdin.readline

n=int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

white_count = 0
blue_count = 0

def count_paper(paper, x, y, size):
    start_color=paper[x][y]

    for i in range(x, x+size):
        for j in range(y,y+size):
            if paper[i][j]!=start_color:
                half=size//2
                count_paper(paper,x,y,half)
                count_paper(paper,x+half,y,half)
                count_paper(paper,x,y+half,half)
                count_paper(paper,x+half,y+half,half)
                return

    if start_color == 0:
        global white_count
        white_count += 1
    else:
        global blue_count
        blue_count += 1

count_paper(paper, 0, 0, n)

print(white_count)
print(blue_count)