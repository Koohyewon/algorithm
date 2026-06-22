def solution(s, skip, index):
    answer=""
    
    alpha="abcdefghijklmnopqrstuvwxyz"
    
    for ch in s:
        cnt=0
        pos=alpha.index(ch)
        
        while cnt<index:
            pos=(pos+1)%26
            
            if alpha[pos] not in skip:
                cnt+=1
        
        answer+=alpha[pos]
        
    return answer