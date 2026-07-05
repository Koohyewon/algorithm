def solution(k, tangerine):
    dic = {}

    for t in tangerine:
        if t in dic:
            dic[t] += 1
        else:
            dic[t] = 1

    cnt = list(dic.values())
    cnt.sort(reverse=True)

    box = 0
    answer = 0

    for c in cnt:
        box += c
        answer += 1

        if box >= k:
            break

    return answer