import sys
input = sys.stdin.readline

N = int(input())

print('? 1')
sys.stdout.flush()
start = int(input())

print('?', N)  
sys.stdout.flush()
end = int(input())

print('!', end - start)  
sys.stdout.flush()