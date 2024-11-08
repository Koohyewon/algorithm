import sys

N,M=map(int,sys.stdin.readline().split())
site={}

for _ in range(1,N+1):
    addless,pw=sys.stdin.readline().split()    
    site[addless]=pw


for _ in range(M):
    addless=sys.stdin.readline().strip()
    sys.stdout.write(str(site[addless])+"\n")
