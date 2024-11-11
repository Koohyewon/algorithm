import sys
input = sys.stdin.readline
output = sys.stdout.write

S = 0
M = int(input().strip()) 

for _ in range(M):
    command = input().strip().split()
        
    if command[0] == "add":
        x = int(command[1]) - 1
        S |= (1 << x)
        
    elif command[0] == "remove":
        x = int(command[1]) - 1
        S &= ~(1 << x)
        
    elif command[0] == "check":
        x = int(command[1]) - 1
        output("1\n" if (S & (1 << x)) != 0 else "0\n")
        
    elif command[0] == "toggle":
        x = int(command[1]) - 1
        S ^= (1 << x)
        
    elif command[0] == "all":
        S = (1 << 20) - 1
        
    elif command[0] == "empty":
        S = 0
