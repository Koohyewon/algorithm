import sys

num = list(map(int, sys.stdin.readline().split()))

if num == sorted(num):
    print("ascending")
elif num == sorted(num, reverse=True):
    print("descending")
else:
    print("mixed")