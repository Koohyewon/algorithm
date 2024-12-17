import sys

s = sys.stdin.readline().strip()

def can_pikachu(s):
    i = 0
    n = len(s)
    
    while i < n:      
        if s[i:i+2] == "pi":
            i += 2
        elif s[i:i+2] == "ka":
            i += 2
        elif s[i:i+3] == "chu":
            i += 3
        else:
            return "NO" 
    
    return "YES" 

print(can_pikachu(s))