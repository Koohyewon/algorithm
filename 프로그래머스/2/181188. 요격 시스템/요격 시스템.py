def solution(targets):
    targets.sort(key=lambda x: x[1])

    answer = 0
    cur_s = -1
    cur_e = -1

    for target in targets:
        s = target[0]
        e = target[1]

        if cur_e == -1:             
            cur_s = s
            cur_e = e
        elif s < cur_e:                
            if s > cur_s:
                cur_s = s
            if e < cur_e:
                cur_e = e
        else:                           
            answer = answer + 1
            cur_s = s
            cur_e = e

    if cur_e != -1:                    
        answer = answer + 1

    return answer