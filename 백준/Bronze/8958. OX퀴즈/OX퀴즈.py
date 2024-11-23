import sys

T=int(sys.stdin.readline())

for _ in range(T):
    OX=sys.stdin.readline()
    cnt,O_cnt = 0,0
    for i in OX:
        if i == "O":
            O_cnt += 1
            cnt += (1*O_cnt)
        else:
            O_cnt = 0

    print(cnt)           