import sys

N,M=map(int,sys.stdin.readline().split())
site={}

for _ in range(1,N+1):
    address,pw=sys.stdin.readline().split()    
    site[address]=pw


for _ in range(M):
    address=sys.stdin.readline().strip()
    sys.stdout.write(str(site[address])+"\n")
