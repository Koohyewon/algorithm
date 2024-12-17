import sys
input = sys.stdin.readline

L = int(input())  
string = input().strip()  

val = 0  
r = 31 
M = 1234567891 

for i in range(L):
    char = ord(string[i]) - ord('a') + 1 
    val += char * (r ** i) 

print(val % M) 