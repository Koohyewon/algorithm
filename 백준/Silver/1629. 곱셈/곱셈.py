import sys
input=sys.stdin.readline

A,B,C=map(int, input().split())

def mod(A,B):
    if B==1:
        return A % C
    else:
        result=mod(A, B//2)
        if B % 2==0:        
            return (result*result) % C
        else:
            return (result*result*A) % C
    
print(mod(A,B))