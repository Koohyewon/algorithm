def solution(nums):
    dic={}
    
    for i in nums:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1        
    
    return min(len(dic), len(nums)//2)