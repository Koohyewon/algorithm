import sys
input=sys.stdin.readline

n=int(input())

def sugar(n):
    for x in range(n // 5, -1, -1):  
        remainder = n - (x * 5)
        if remainder % 3 == 0:
            y = remainder // 3
            return x + y  
    return -1 

print(sugar(n))