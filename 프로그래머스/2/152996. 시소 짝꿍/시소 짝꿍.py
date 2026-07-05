def solution(weights):
    weights.sort()

    dic = {}
    answer = 0

    for w in weights:
        if w in dic:
            answer += dic[w]

        if w * 2 % 3 == 0 and w * 2 // 3 in dic:
            answer += dic[w * 2 // 3]

        if w * 2 % 4 == 0 and w * 2 // 4 in dic:
            answer += dic[w * 2 // 4]

        if w * 3 % 4 == 0 and w * 3 // 4 in dic:
            answer += dic[w * 3 // 4]

        if w in dic:
            dic[w] += 1
        else:
            dic[w] = 1

    return answer