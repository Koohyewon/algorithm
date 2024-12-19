import sys
input = sys.stdin.read
lines = input().splitlines()

def balance(string):
    stack = []
    for char in string:
        if char in '([':
            stack.append(char)
        elif char == ')':
            if not stack or stack[-1] != '(':
                return "no"
            stack.pop()
        elif char == ']':
            if not stack or stack[-1] != '[':
                return "no"
            stack.pop()
    return "yes" if not stack else "no"


for line in lines:
    if line == '.':
        break
    print(balance(line))