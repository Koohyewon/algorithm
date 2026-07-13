def solution(keymap, targets):
    dic = {}

    for key in keymap:
        cnt = 1
        for ch in key:
            if ch not in dic:
                dic[ch] = cnt
            else:
                if cnt < dic[ch]:
                    dic[ch] = cnt
            cnt += 1

    answer = []
    
    for target in targets:
        total = 0
        ok = True

        for ch in target:
            if ch not in dic:
                ok = False
                break
            total += dic[ch]

        if ok:
            answer.append(total)
        else:
            answer.append(-1)

    return answer