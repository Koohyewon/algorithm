import sys

m = int(sys.stdin.readline())
s = [0] * 21

for i in range(m):
    cmd = sys.stdin.readline().strip().split()

    if cmd[0] == "all":
        s = [1] * 21
    elif cmd[0] == "empty":
        s = [0] * 21
        
    elif cmd[0] == "add":
        s[int(cmd[1])] = 1 
    elif cmd[0] == "remove":
        s[int(cmd[1])] = 0 
    elif cmd[0] == "check":
        if s[int(cmd[1])] == 0:
            print(0)
        else:
            print(1)
    elif cmd[0] == "toggle":
        if s[int(cmd[1])] == 0: 
            s[int(cmd[1])] = 1
        else:
            s[int(cmd[1])] = 0
