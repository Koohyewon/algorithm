def solution(d, budget):
    d=sorted(d)
    
    cnt=0
    for i in d:
        if i<=budget:
            budget-=i; cnt+=1
        else: break
            
    return cnt