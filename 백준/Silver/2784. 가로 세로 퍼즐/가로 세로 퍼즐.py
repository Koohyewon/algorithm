from itertools import permutations
import sys

words = [sys.stdin.readline().strip() for _ in range(6)]

def isValid(horizontal, vertical):
    for i in range(3):
        for j in range(3):
            if horizontal[i][j] != vertical[j][i]:
                return False
    return True

def isPuzzle(words):
    for perm in permutations(words):
        horizontal = perm[:3]
        vertical = perm[3:]

        if isValid(horizontal, vertical):
            return horizontal

    return 0

result = isPuzzle(words)

if result == 0:
    print(0)
else:
    for line in result:
        print(line)
