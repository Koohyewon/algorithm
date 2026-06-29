def solution(dartResult):
    answer = []
    
    i=0
    
    while i <len(dartResult):
        if dartResult[i]>="0" and dartResult[i]<="9":
            if i+1<len(dartResult) and dartResult[i] == "1" and dartResult[i+1]=="0":
                answer.append(10)
                i+=1
                
            else:
                answer.append(int(dartResult[i]))                       

        elif dartResult[i]=="S":
            answer[-1] **=1

        elif dartResult[i]=="D":
            answer[-1]**=2

        elif dartResult[i]=="T":
            answer[-1] **=3

        elif dartResult[i]=="*":
            answer[-1] *=2
            if len(answer)>=2:
                answer[-2]*=2

        elif dartResult[i]=="#":
            answer[-1] *=-1

        i += 1

    return sum(answer)