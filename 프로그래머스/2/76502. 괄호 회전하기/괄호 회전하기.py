def solution(s):
    answer = 0

    open_ch="([{"
    close_ch=")]}"

    for i in range(len(s)):
        rotate=s[i:]+s[:i]
        stack=[]

        for ch in rotate:
            if ch in open_ch: stack.append(ch)                

            else:
                if not stack: break

                if open_ch.index(stack[-1]) == close_ch.index(ch): stack.pop()                    
                else: break
                    
        else:
            if not stack: answer += 1
            
    return answer