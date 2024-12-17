import sys
input = sys.stdin.readline

L = int(input())  
string = input().strip()  

val = 0  
r = 31 

for i in range(L):
    char_value = ord(string[i]) - ord('a') + 1 
    val += char_value * (r ** i) 

print(val) 
