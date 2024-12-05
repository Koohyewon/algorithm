import sys

k = int(sys.stdin.readline())

stack = []
for _ in range(k):
    num = int(sys.stdin.readline())
    if num != 0:
        stack.append(num)
    elif num == 0:
        stack.pop()

sum = 0
while len(stack) > 0:
    sum += stack.pop()
print(sum)