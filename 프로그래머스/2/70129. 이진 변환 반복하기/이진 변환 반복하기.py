def binary(n):
    result = ""
    while n > 0:
        result = result + str(n % 2)  
        n //= 2                        
    return result

def solution(s):
    cnt,zero = 0,0

    while s!="1":        
        one=0
        for i in s:
            if i == "1": one += 1
            else: zero += 1
        s=binary(one)
        cnt+=1
        
    return [cnt,zero]