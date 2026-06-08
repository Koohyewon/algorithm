def solution(name, yearning, photos):
    answer = []
    score={}
    for i in range(len(name)):
        score[name[i]]=yearning[i]

    for photo in photos:
        cnt=0
        for person in photo:
            if person in score:   
                cnt+=score[person] 
        answer.append(cnt)
    return answer