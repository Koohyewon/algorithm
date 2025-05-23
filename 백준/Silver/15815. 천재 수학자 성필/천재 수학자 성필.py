import sys
input=sys.stdin.readline

cmds = input().strip()
stack = []

for cmd in cmds:
    if cmd not in '+-*/':   
        stack.append(int(cmd))
    else:
        b = stack.pop()
        a = stack.pop()
        if cmd == '+':
            stack.append(a + b)
        elif cmd == '-':
            stack.append(a - b)
        elif cmd == '*':
            stack.append(a * b)
        elif cmd == '/':
            stack.append(a // b)

print(stack[0])