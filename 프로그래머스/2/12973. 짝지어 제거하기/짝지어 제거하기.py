def solution(s):
    answer = 1
    stack=[]
    
    for i in s: #s문자열 길이만큼 반복 O(n)
        if stack and i == stack[-1]:
            stack.pop()
        else:
            stack.append(i)
            
    if stack:
        answer = 0
        
    return answer